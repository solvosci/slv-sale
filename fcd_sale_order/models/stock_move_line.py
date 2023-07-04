# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    partner_id = fields.Many2one(
        related="move_id.partner_id",
        store=True,
        string="Partner"
    )
    fcd_origin_lot_id = fields.Many2one(
        related="lot_id.fcd_origin_lot_id",
        store=True,
    )
    sale_date_order = fields.Datetime(
        related="move_id.sale_line_id.order_id.date_order",
        store=True,
    )
    sale_currency_id = fields.Many2one(
        related="move_id.sale_line_id.currency_id",
    )

    fcd_purchase_price_kg = fields.Float(
        string="Purchase Price (kg)",
        digits="Product Price",
        compute="_compute_fcd_price_data_kg",
        store=True,
    )
    sale_price_kg = fields.Float(
        string="Sale Price (kg)",
        digits="Product Price",
        compute="_compute_fcd_price_data_kg",
        store=True,
    )
    sale_margin = fields.Monetary(
        string="Margin",
        digits="Product Price",
        compute="_compute_fcd_price_data_kg",
        currency_field="sale_currency_id",
        store=True,
    )
    fcd_document_id = fields.Many2one(related='fcd_document_line_id.fcd_document_id')
    fcd_document_line_id = fields.Many2one('fcd.document.line', compute='_compute_fcd_document_line_id', store=True)

    @api.depends(
        "product_uom_id",
        "qty_done",
        "lot_id.fcd_document_line_price_real_kg",
        "lot_id.fcd_origin_lot_id.fcd_document_line_price_real_kg",
        "move_id.sale_line_id.product_uom",
        "move_id.sale_line_id.price_unit",
    )
    def _compute_fcd_price_data_kg(self):
        uom_kg = self.env.ref("uom.product_uom_kgm")
        uom_kg_categ = self.env.ref("uom.product_uom_categ_kgm")
        # Prevent non-compatible UoMs
        sml_update = self.filtered(
            lambda x: x.product_uom_id.category_id == uom_kg_categ
        )
        for sml in sml_update:
            lot_id = sml.fcd_origin_lot_id or sml.lot_id
            # TODO lot_id.sudo() if needed
            sml.fcd_purchase_price_kg = (
                lot_id
                and lot_id.fcd_document_line_price_real_kg
                or 0.0
            )
            # TODO move_id.sudo() if needed
            sale_line_id = sml.move_id.sale_line_id
            sml.sale_price_kg = (
                sale_line_id
                and sale_line_id.price_unit * sale_line_id.product_uom.factor
            )
            quantity_kg = sml.product_uom_id._compute_quantity(sml.qty_done, uom_kg)
            sml.sale_margin = quantity_kg*(sml.sale_price_kg - sml.fcd_purchase_price_kg)
        # Other UoM stock move lines
        (self - sml_update).write({
            "fcd_purchase_price_kg": 0.0,
            "sale_price_kg": 0.0,
            "sale_margin": 0.0,
        })

    @api.depends('lot_id.fcd_document_line_id', 'lot_id.fcd_origin_lot_id.fcd_document_line_id')
    def _compute_fcd_document_line_id(self):
        for record in self:
            if record.lot_id.fcd_document_line_id:
                record.fcd_document_line_id = record.lot_id.fcd_document_line_id
            elif record.lot_id.fcd_origin_lot_id.fcd_document_line_id:
                record.fcd_document_line_id = record.lot_id.fcd_origin_lot_id.fcd_document_line_id
            else:
                record.fcd_document_line_id = False

    @api.model
    def read_group(
        self,
        domain,
        fields,
        groupby,
        offset=0,
        limit=None,
        orderby=False,
        lazy=True
    ):
        """
        TODO be careful with performance!!!
        """
        res = super(StockMoveLine, self).read_group(
            domain,
            fields,
            groupby,
            offset=offset,
            limit=limit,
            orderby=orderby,
            lazy=lazy
        )
        group_fields = ["fcd_purchase_price_kg", "sale_price_kg"]
        # fields should be filled like "field1:sum"adnmi
        fields = [x.split(":")[0] for x in fields]
        if any([x in fields for x in group_fields]):
            for line in res:
                line.update({
                    "fcd_purchase_price_kg": 0.0,
                    "sale_price_kg": 0.0,
                })
                # TODO float_is_zero
                if abs(line["qty_done"]) > 0.0:
                    total_line_purchase = 0.0
                    total_line_sale = 0.0
                    lines = self.search(line.get("__domain", domain))
                    for line_item in lines:
                        total_line_purchase += (
                            line_item.qty_done*line_item.fcd_purchase_price_kg
                        )
                        total_line_sale += (
                            line_item.qty_done*line_item.sale_price_kg
                        )
                    line.update({
                        "fcd_purchase_price_kg": total_line_purchase/line["qty_done"],
                        "sale_price_kg": total_line_sale/line["qty_done"],
                    })

        return res

    def action_open_stock_quant(self):
        self.ensure_one()
        stock_quant_ids = self.env['stock.quant'].search([
            ('location_id.usage','=', 'internal'),
            ('product_id', '=', self.product_id.id)
        ])

        wizard_ids = self.env['fcd.stock.quant.wizard']
        for record in stock_quant_ids:
            wizard_ids += self.env['fcd.stock.quant.wizard'].create({
                'stock_quant_id': record.id,
                'stock_move_line_id': self.id,
            })

        return {
            'name': _('Stock Quant'),
            'res_model': 'fcd.stock.quant.wizard',
            'view_mode': 'list',
            'view_type': 'list',
            'domain': [('id', 'in', wizard_ids.ids)],
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': {'inventory_mode': True}
        }
