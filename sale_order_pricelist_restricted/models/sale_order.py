# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    allowed_pricelist_ids = fields.Many2many(
        comodel_name="product.pricelist",
        string="Allowed Pricelists",
        compute="_compute_allowed_pricelist_ids",
        help="Technical field to filter pricelists for this order",
    )

    @api.depends("partner_id", "company_id")
    def _compute_allowed_pricelist_ids(self):
        pp_obj = self.env["product.pricelist"]
        order_w_partner_ids = self.filtered(lambda x: x.partner_id)
        for order in order_w_partner_ids:
            order.allowed_pricelist_ids = pp_obj.search(
                [
                    ("company_id", "in", [False, order.company_id.id]),
                    "|",
                        ("sale_order_selectable", "=", True),
                        ("sale_order_exclusive_partner_id", "=", order.partner_id.id),
                ]
            ) | order.partner_id.with_company(order.company_id).property_product_pricelist
        (self - order_w_partner_ids).write({"allowed_pricelist_ids": False})
