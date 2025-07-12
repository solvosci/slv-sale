# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _prepare_invoice_line(self):
        res = super()._prepare_invoice_line()
        if self.currency_id != self.company_id.currency_id and self.order_id.custom_rate_enabled:
            context = {
                "custom_rate": self.order_id.custom_rate,
                "to_currency": self.company_id.currency_id,
            }
            original_currency = self.company_id.currency_id.with_context(**context)
            res["original_price_unit"] = original_currency._convert(
                self.price_unit,
                self.currency_id,
                self.company_id,
                # TODO context_date, indeed, but it seems to be unnecessary
                self.order_id.date_order.date(),
            )
        return res
