# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


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