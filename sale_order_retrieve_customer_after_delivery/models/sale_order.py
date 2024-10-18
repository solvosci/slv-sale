# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_shipping_id')
    def _onchange_partner_shipping_id(self):
        for order in self:
            order.with_context(skip_change_shipping=True).partner_id = order.partner_shipping_id.commercial_partner_id
        
    @api.depends('partner_id')
    def _compute_partner_shipping_id(self):
        if self.env.context.get("skip_change_shipping", False):
            pass
        else:
            super()._compute_partner_shipping_id()
