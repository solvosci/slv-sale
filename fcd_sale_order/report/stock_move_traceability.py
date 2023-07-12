# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from psycopg2.extensions import AsIs

from odoo import fields, models, tools


class StockMoveTraceability(models.Model):

    _name = "fcd.stock.move.traceability"
    _description = "Stock Move FCD Traceability"
    _auto = False

    product_id = fields.Many2one('product.product', readonly=True)
    lot_id = fields.Many2one('stock.production.lot', readonly=True)
    fcd_document_id = fields.Many2one('fcd.document', readonly=True)

    purchase_order_id = fields.Many2one('purchase.order', readonly=True)
    po_date_done = fields.Datetime('Purchase Date', readonly=True)
    po_partner_id = fields.Many2one('res.partner', readonly=True)
    po_qty_done = fields.Float(readonly=True)
    po_sp_id = fields.Many2one(
        "stock.picking",
        readonly=True,
        string="Purchase Delivery Note",
    )
    po_sml_qty_done = fields.Float(
        readonly=True,
        string="Received Qty",
    )

    sale_order_id = fields.Many2one('sale.order', readonly=True)
    so_partner_id = fields.Many2one('res.partner', readonly=True)
    so_qty_done = fields.Float(readonly=True)
    so_date_done = fields.Datetime('Sale Date', readonly=True)
    so_sp_id = fields.Many2one(
        "stock.picking",
        readonly=True,
        string="Sales Delivery Note",
    )
    so_sml_qty_done = fields.Float(
        readonly=True,
        string="Delivered Qty",
    )

    def init(self):
        """
        Starting from a sales stock move line we could reach more than one
        purchase stock move line, so smls.id is not valid as unique id, it
        could be listed twice or more. Then, using purchase sml for id
        definition formula is required.
        The current definition, also based on purchase sml, will work for
        max(sml) < 10M. It this value is reached, simply try multiply by
        100M instead of 10M
        """
        query = """
            SELECT
                (10000000*smls.id::bigint + coalesce(smlp.id, 0)) id,
                spp.date_done po_date_done,
                spp.partner_id po_partner_id,
                smls.product_id product_id,
                smls.lot_id lot_id,
                fcddl.fcd_document_id fcd_document_id,
                pol.order_id purchase_order_id,
                smlp.qty_done po_qty_done,
	            spp.id po_sp_id,
                spp.date_done po_sp_date_done,                
	            smlp.qty_done po_sml_qty_done,                
                sol.order_partner_id so_partner_id,
                sps.partner_id so_sp_partner_id,
                smls.qty_done so_qty_done,
                sps.date_done so_date_done,
                sol.order_id sale_order_id,
                sps.id so_sp_id,
                smls.qty_done so_sml_qty_done
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
            LEFT JOIN
                fcd_document_line fcddl
                ON fcddl.id=smls.fcd_document_line_id
            LEFT JOIN
                purchase_order_line pol
                ON pol.fcd_document_line_id=smls.fcd_document_line_id
            LEFT JOIN
                stock_move smp
                ON smp.purchase_line_id=pol.id
            LEFT JOIN
                stock_move_line smlp
                ON smlp.move_id=smp.id
            LEFT JOIN
                stock_picking spp
                ON spp.id=smp.picking_id
            WHERE
                smls.state='done'
        """
        tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute(
            "CREATE OR REPLACE VIEW %s AS (%s)", (AsIs(self._table), AsIs(query))
        )
