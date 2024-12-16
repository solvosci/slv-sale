# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model_create_multi
    def create(self, vals_list):
        # When creating records, we need to update affected pricelists
        res = super().create(vals_list)
        res.sudo().property_product_pricelist._update_salesman_user_ids()
        return res

    def write(self, values):
        pricelist_ids = self.env["product.pricelist"].sudo()
        pricelist_update = any(
            field in values
            for field in ["user_id", "property_product_pricelist"] 
        )
        if pricelist_update:
            pricelist_ids = self.sudo().property_product_pricelist
        res = super().write(values)
        pricelist_ids |= self.sudo().property_product_pricelist
        if pricelist_ids:
            pricelist_ids._update_salesman_user_ids()
        return res

    # TODO unlink support