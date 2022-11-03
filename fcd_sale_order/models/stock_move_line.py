# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

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
    sale_margin = fields.Float(
        string="Margin",
        digits="Product Price",
        compute="_compute_fcd_price_data_kg",
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
            lot_id = sml.lot_id.fcd_origin_lot_id or sml.lot_id
            # TODO lot_id.sudo() if needed
            sml.fcd_purchase_price_kg = (
                lot_id
                and lot_id.fcd_document_line_price_real_kg
                or 0.0
            )
            # TODO move_id.sudo() if needed
            sale_line_id = sml.move_id.sale_line_id
            quantity_kg = (
                sale_line_id
                and sale_line_id.product_uom._compute_quantity(sml.qty_done, uom_kg)
                or 0.0
            )
            sml.sale_price_kg = (
                sale_line_id
                and quantity_kg
                and sale_line_id.price_unit * (sml.qty_done / quantity_kg)
            )
            sml.sale_margin = quantity_kg*(sml.sale_price_kg - sml.fcd_purchase_price_kg)
        # Other UoM stock move lines
        (self - sml_update).write({
            "fcd_purchase_price_kg": 0.0,
            "sale_price_kg": 0.0,
            "sale_margin": 0.0,
        })
