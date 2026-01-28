# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    offer_price = fields.Boolean()

    @api.onchange("applied_on")
    def _onchange_offer_price(self):
        if self.applied_on == '1_product':
            self.offer_price = True
        else:
            self.offer_price = False
