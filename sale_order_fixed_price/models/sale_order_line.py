# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, api
from odoo.tools import float_is_zero


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _compute_price_unit(self):
        if self.env.context.get('not_change_prices_from_pricelist'):
            return super()._compute_price_unit()

        precision_price = self.env['decimal.precision'].precision_get('Product Price')

        save_values = {
            line: {
                'price_unit': line.price_unit,
                'discount': line.discount,
            }
            for line in self if not float_is_zero(line.price_unit, precision_digits=precision_price)
        }

        super()._compute_price_unit()

        for line, values in save_values.items():
            line.write(values)
