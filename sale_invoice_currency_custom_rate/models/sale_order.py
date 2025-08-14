# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, models, fields


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "currency.custom.rate.mixin"]

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res.update(self._prepare_invoice_custom_rate_vals())
        return res
