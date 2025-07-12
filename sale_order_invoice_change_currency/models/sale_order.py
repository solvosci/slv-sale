# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_rate_enabled = fields.Boolean(
        string="Apply Custom Currency Rate",
        default=False,
        copy=False,
        help="Apply custom currency rate to convert amounts between the "
        "currency on the invoice and last currency",
    )
    custom_rate_enabled_visible = fields.Boolean(
        string="Is 'Apply Custom Currency Rate' visible",
        compute="_compute_custom_rate_enabled_visible",
    )

    custom_rate = fields.Float(
        digits=(12, 6),
        default=1,
        store=True,
        readonly=False,
        copy=False,
        compute="_compute_custom_rate",
        help="Set new currency rate to apply on the sales order invoices.\n"
        "This rate will be taken in order to convert amounts between the "
        "currency on the invoice and last currency",
    )

    @api.depends("state", "currency_id", "company_id")
    def _compute_custom_rate_enabled_visible(self):
        # Only Invoicing Managers can set custom rate, when order currency is
        # different and company id, and only for non locked or cancel orders
        order_custom_rate_visible = self.browse([])
        if self.env.user.has_group(
            "account.group_account_manager"
        ):
            order_custom_rate_visible = self.filtered(
                lambda x: (
                    x.state not in ["draft", "done"]
                    and x.currency_id != x.company_id.currency_id
                )
            )
        if order_custom_rate_visible:
            order_custom_rate_visible.custom_rate_enabled_visible = True
        (self - order_custom_rate_visible).custom_rate_enabled_visible = False

    @api.depends("company_id", "currency_id", "date_order", "custom_rate_enabled")
    def _compute_custom_rate(self):
        """
        Compute the custom rate from the original currency when the invoice
        was created to the current currency. The custom rate field is
        editable, but it will not change if custom rate is zero or the
        current currency and the original currency are the same
        """
        for order in self:
            if not order.currency_id or not order.company_id:
                order.custom_rate = 1.0
                continue
            date = order.date_order.date() or fields.Date.context_today(order)
            # Proper original currency management (for three or more active currencies)
            # from_currency = order.original_currency_id or order.currency_id
            from_currency = order.company_id.currency_id
            order.custom_rate = from_currency._get_conversion_rate(
                from_currency, order.currency_id, order.company_id, date,
            )

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        if self.currency_id != self.company_id.currency_id and self.custom_rate_enabled:
            res.update({
                "custom_rate": self.custom_rate,
                "original_currency_id": self.company_id.currency_id.id,
            })
        return res
    
    def _create_invoices(self, grouped=False, final=False):
        moves = super()._create_invoices(grouped=grouped, final=final)
        moves.filtered(lambda x: not x.is_original_currency).action_account_change_currency()
        return moves
