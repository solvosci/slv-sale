# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, models, fields


class Currency(models.Model):
    _inherit = "res.currency"
    _description = "Currency"

    @api.model
    def _get_conversion_rate(self, from_currency, to_currency, company, date):
        res = super(Currency, self)._get_conversion_rate(from_currency, to_currency, company, date)
        ctx = self.env.context.copy()
        if ctx.get('force_custom_rate'):
            sale_id = self.env['sale.order'].browse(ctx['active_id']).exists()
            res = to_currency.rate / sale_id.custom_rate
        return res