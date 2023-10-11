# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, tools
from psycopg2.extensions import AsIs


class FcdSaleReportInvoice(models.Model):
    _name = "fcd.sale.report.invoice"
    _description = "Sales & Invoice Margin per Operation"
    _auto = False

    date_order = fields.Datetime(readonly=True)
    origin_warehouse_id = fields.Many2one('stock.warehouse', readonly=True)
    po_partner_id = fields.Many2one('res.partner', readonly=True)
    so_partner_id = fields.Many2one('res.partner', readonly=True)
    product_id = fields.Many2one('product.product', readonly=True)
    lot_id = fields.Many2one('stock.production.lot', readonly=True)
    so_sml_qty_done = fields.Float(digits="Product Unit of Measure", readonly=True)
    smls_qty_invoiced = fields.Float(digits="Product Unit of Measure", readonly=True)
    sale_price_kg = fields.Float(digits="Product Unit of Measure", readonly=True)
    fcd_purchase_price_kg = fields.Float(digits="Product Unit of Measure", readonly=True)
    smls_amount_base = fields.Monetary(digits="Product Unit of Measure", readonly=True)
    smls_price_subtotal = fields.Monetary(digits="Product Unit of Measure", readonly=True)
    margin_net = fields.Monetary(digits="Product Unit of Measure", readonly=True)
    margin_net_invoiced = fields.Monetary(digits="Product Unit of Measure", readonly=True)
    margin_pct = fields.Float(digits="Product Unit of Measure", readonly=True)
    margin_pct_invoiced = fields.Float(digits="Product Unit of Measure", readonly=True)
    currency_id = fields.Many2one('res.currency', readonly=True)
    company_id = fields.Many2one('res.company', readonly=True)

    def init(self):
        query = """
            SELECT
                smls.id id,
                so.date_order date_order,
                -- Origen almacén, cogemos por el tipo de picking de la compra,
                --  para no ir al stock.move de la compra, que lo complicaría
                --  (puede hacer más de uno)
                sptp.warehouse_id origin_warehouse_id,
                po.partner_id po_partner_id,
                so.partner_id so_partner_id,
                smls.product_id product_id,
                smls.lot_id lot_id,
                smls.qty_done so_sml_qty_done,
                /**/coalesce(
                    (select sum(aml.quantity)
                    from stock_move_invoice_line_rel smilr
                    inner join account_move_line aml
                        on aml.id=smilr.invoice_line_id
                    where smilr.move_id=smls.move_id),
                    0.0
                ) smls_qty_invoiced,/**/
                smls.sale_price_kg sale_price_kg,
                smls.fcd_purchase_price_kg fcd_purchase_price_kg,
                (smls.sale_price_kg*smls.qty_done) smls_amount_base,
                /**/coalesce(
                    (select sum(aml.price_subtotal)
                    from stock_move_invoice_line_rel smilr
                    inner join account_move_line aml
                        on aml.id=smilr.invoice_line_id
                    where smilr.move_id=smls.move_id),
                    0.0
                ) smls_price_subtotal,/**/
                smls.sale_margin margin_net,
                -- Neto facturado (margen absoluto), nos basamos en
                --  https://github.com/solvosci/slv-sale/blob/14.0/fcd_sale_order/models/stock_move_line.py#L79C31-L79C90
                -- => no solo cogemos cantidad de factura, también el precio, CONFIRMAR
                /**/coalesce(
                    (select sum(aml.quantity*(aml.price_unit - smls.fcd_purchase_price_kg))
                    from stock_move_invoice_line_rel smilr
                    inner join account_move_line aml
                        on aml.id=smilr.invoice_line_id
                    where smilr.move_id=smls.move_id),
                    0.0
                ) margin_net_invoiced,/**/
                -- Margen (%)
                -- => lo hacemos solo con precios, CONFIRMAR
                case
                    when fcd_purchase_price_kg > 0.0
                    then (smls.sale_price_kg/smls.fcd_purchase_price_kg) - 1
                    else 0.0
                end margin_pct,
                -- Margen facturado (%)
                -- => lo hacemos solo con precios, CONFIRMAR
                -- => la fórmula es especialmente compleja por la posibilidad de más de una
                --    factura con importes distintos
                /**/coalesce(
                    (select
                        (sum(V.quantity*V.price_mrg)/sum(V.quantity)) - 1
                    from
                        (select
                            aml.quantity,
                            case when smls.fcd_purchase_price_kg > 0.0 then (aml.price_unit/smls.fcd_purchase_price_kg) else 0.0 end price_mrg
                        from stock_move_invoice_line_rel smilr
                        inner join account_move_line aml
                            on aml.id=smilr.invoice_line_id
                        where smilr.move_id=smls.move_id) V
                    ),
                    0.0
                ) margin_pct_invoiced,/**/
                sol.currency_id currency_id,
                smls.company_id company_id
            FROM
                stock_move_line smls
            INNER JOIN
                stock_move sms
                ON sms.id=smls.move_id
            INNER JOIN
                stock_picking sps
                ON sps.id=sms.picking_id
            INNER JOIN
                sale_order_line sol
                ON sol.id=sms.sale_line_id
            INNER JOIN
                sale_order so
                ON so.id=sol.order_id
            LEFT JOIN
                fcd_document_line fcddl
                ON fcddl.id=smls.fcd_document_line_id
            LEFT JOIN
                purchase_order_line pol
                ON pol.fcd_document_line_id=smls.fcd_document_line_id
            LEFT JOIN
                purchase_order po
                ON po.id=pol.order_id
            LEFT JOIN
                stock_picking_type sptp
                ON sptp.id=po.picking_type_id
            WHERE
                smls.state='done'
            /**/order by so.date_order desc, id desc/**/
        """
        tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute(
            "CREATE OR REPLACE VIEW %s AS (%s)", (AsIs(self._table), AsIs(query))
        )
