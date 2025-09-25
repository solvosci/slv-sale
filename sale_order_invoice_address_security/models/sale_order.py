# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_invoice_address_visible = fields.Boolean(compute="_compute_is_invoice_address_visible")

    # The @api.depends is used like a workround because the precompute doesn´t initialize the field
    # before an order ir created
    @api.depends('state')
    def _compute_is_invoice_address_visible(self):
        self.update({'is_invoice_address_visible': False})
        if self.env.user.has_group('account.group_account_invoice'):
            self.update({'is_invoice_address_visible': True})
