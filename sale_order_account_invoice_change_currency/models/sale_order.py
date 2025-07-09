# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_rate = fields.Float(
        digits=(12, 6),
        default=1,
        help="Set new currency rate to apply on the invoice\n."
        "This rate will be taken in order to convert amounts between the "
        "currency on the invoice and last currency",
        tracking=True,
        compute="_compute_custom_rate",
        store=True,
    )
    is_company_currency = fields.Boolean(compute="_compute_company_currency_id")
    is_custom_rate = fields.Boolean()

    @api.depends("currency_id")
    def _compute_company_currency_id(self):
        for order in self:
            order.is_company_currency = order.currency_id == self.env.company.currency_id

    @api.depends("currency_id", "is_custom_rate")
    def _compute_custom_rate(self):
        for order in self:
            if order.currency_id == order.company_id.currency_id:
                order.custom_rate = 1.0
            else:
                order.custom_rate = order.currency_id.rate

    def action_view_invoice(self):
        res = super(SaleOrder, self).action_view_invoice()
        invoices = self.mapped('invoice_ids')
        if self.is_custom_rate:
            invoices.original_currency_id = self.env.company.currency_id
            invoices.custom_rate = self.custom_rate
            for line in invoices.invoice_line_ids:
                line.original_price_unit /= invoices.custom_rate
            invoices.action_account_change_currency()
            ctx = self.env.context.copy()
            ctx['force_custom_rate'] = True
            invoices.invoice_line_ids.with_context(ctx)._recompute_debit_credit_from_amount_currency()
        return res