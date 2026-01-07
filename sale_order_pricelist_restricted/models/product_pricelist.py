# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    sale_order_selectable = fields.Boolean(
        string="Is selectable in Sales Orders",
        default=False,
    )
    sale_order_exclusive_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Exclusive Partner for Sales Orders",
    )

    salesman_user_ids = fields.Many2many(
        comodel_name="res.users",
        string="Salesman Users",
    )

    def _update_salesman_user_ids(self):
        # TODO improve this!
        #  property_product_pricelist is a headache!
        all_partners = self.env["res.partner"].search([])
        for pricelist in self:
            pricelist.salesman_user_ids = all_partners.filtered(
                lambda x: x.property_product_pricelist == pricelist
            ).user_id
