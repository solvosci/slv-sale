# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models
from odoo.tools import float_is_zero


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    price_unit_wd = fields.Float(
         string="Unit Price W/discount",
         compute="_compute_price_unit_wd",
         store=True,
         readonly=False,
         help="Technical field for pending invoicing amount data",
    )

    @api.depends("price_subtotal", "product_uom_qty")
    def _compute_price_unit_wd(self):
        # Lines without product have no rounding, so float_is_zero should fail
        lines_wp = self.filtered(lambda x: x.product_id)
        for line in lines_wp:
            if float_is_zero(
                line.product_uom_qty,
                precision_rounding=line.product_id.uom_id.rounding
            ):
                line.price_unit_wd = 0.0
            else:
                line.price_unit_wd = (
                    line.price_subtotal / line.product_uom_qty
                )
        for line in (self - lines_wp):
            line.price_unit_wd = 0.0
