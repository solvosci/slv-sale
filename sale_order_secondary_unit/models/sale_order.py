# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models
from odoo.tools.float_utils import float_compare, float_round


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    secondary_uom_qty = fields.Float(
        string="Secondary Qty", digits="Product Unit of Measure"
    )
    secondary_uom_id = fields.Many2one(
        comodel_name="product.secondary.unit",
        string="Secondary uom",
        ondelete="restrict",
    )

    # @api.onchange("secondary_uom_id", "secondary_uom_qty")
    # def _onchange_secondary_uom(self):
    #     if not self.secondary_uom_id:
    #         return
    #     factor = self.secondary_uom_id.factor * self.product_uom.factor
    #     qty = float_round(
    #         self.secondary_uom_qty * factor,
    #         precision_rounding=self.product_uom.rounding,
    #     )
    #     if (
    #         float_compare(
    #             self.product_uom_qty, qty, precision_rounding=self.product_uom.rounding
    #         )
    #         != 0
    #     ):
    #         self.product_uom_qty = qty

    # @api.onchange("product_uom_qty")
    # def _onchange_product_uom_qty_sale_order_secondary_unit(self):
    #     if not self.secondary_uom_id:
    #         return
    #     factor = self.secondary_uom_id.factor * self.product_uom.factor
    #     qty = float_round(
    #         self.product_uom_qty / (factor or 1.0),
    #         precision_rounding=self.secondary_uom_id.uom_id.rounding,
    #     )
    #     if (
    #         float_compare(
    #             self.secondary_uom_qty,
    #             qty,
    #             precision_rounding=self.secondary_uom_id.uom_id.rounding,
    #         )
    #         != 0
    #     ):
    #         self.secondary_uom_qty = qty

    # @api.onchange("product_uom")
    # def _onchange_product_uom_sale_order_secondary_unit(self):
    #     if not self.secondary_uom_id:
    #         return
    #     factor = self.product_uom.factor * self.secondary_uom_id.factor
    #     qty = float_round(
    #         self.product_uom_qty / (factor or 1.0),
    #         precision_rounding=self.product_uom.rounding,
    #     )
    #     if (
    #         float_compare(
    #             self.secondary_uom_qty,
    #             qty,
    #             precision_rounding=self.product_uom.rounding,
    #         )
    #         != 0
    #     ):
    #         self.secondary_uom_qty = qty

    @api.onchange("product_id")
    def _onchange_product_id_sale_order_secondary_unit(self):
        self.secondary_uom_id = self.product_id.sale_secondary_uom_id
