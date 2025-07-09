# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    # @api.model
    # def create(self, values):
    #     invoice = super(AccountMove, self).create(values)
    #     if self.env.company.currency_id != invoice.currency_id:
    #         today = fields.Date.context_today(self)
    #         ctx = self.env.context.copy()
    #         if ctx.get('active_model') == 'sale.order' and ctx.get('active_id'):
    #             sale_id = self.env['sale.order'].browse(ctx['active_id']).exists()
    #             invoice.original_currency_id = self.env.company.currency_id
    #             invoice.custom_rate = sale_id.custom_rate
    #             for line in invoice.invoice_line_ids:
    #                 line.original_price_unit /= invoice.custom_rate
    #             invoice.action_account_change_currency()
    #     return invoice
