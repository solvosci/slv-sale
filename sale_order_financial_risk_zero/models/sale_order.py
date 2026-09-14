# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import models, _, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def evaluate_risk_message(self, partner):
        res = super().evaluate_risk_message(partner)
        if res:
            return res

        risk_amount = self.currency_id._convert(
            self.amount_total,
            partner.risk_currency_id,
            self.company_id,
            self.date_order and self.date_order.date() or fields.Date.context_today(self),
            round=False,
        )

        if partner.risk_sale_order_include and (
            (partner.risk_total + risk_amount) >= partner.credit_limit
        ):
            return _("This sale order exceeds the financial risk.\n")
        else:
            return ""
