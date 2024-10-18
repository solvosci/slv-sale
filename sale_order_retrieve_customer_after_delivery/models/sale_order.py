# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_shipping_2_id = fields.Many2one(
        comodel_name='res.partner',
        string="Delivery Address (new)",
        required=True,
        check_company=True,
        # index='btree_not_null',
    )    

    @api.onchange('partner_shipping_2_id')
    def _onchange_partner_shipping_2_id(self):
        self.partner_shipping_id = self.partner_shipping_2_id
        self.partner_id = self.partner_shipping_2_id.commercial_partner_id
        
    @api.depends("partner_shipping_2_id")
    def _compute_partner_shipping_id(self):
        # Overridden default behavior:
        # https://github.com/odoo/odoo/blob/98d9f02f89b9f04c9d2d3bf0ba73c4778d511c4b/addons/sale/models/sale_order.py#L363-L366
        for order in self:
            order.partner_shipping_id = order.partner_shipping_2_id
