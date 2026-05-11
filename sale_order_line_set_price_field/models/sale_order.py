# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, _, fields, api
from odoo.exceptions import ValidationError

SET_PRICE_SELECTION = [
    ("yes", "Yes"),
    ("no", "No"),
]

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    set_price = fields.Selection(
        selection=SET_PRICE_SELECTION,
    )


class SaleOrder(models.Model):
    _inherit = "sale.order"

    set_price_lines = fields.Selection(
        selection=SET_PRICE_SELECTION,
    )

    @api.onchange("set_price_lines")
    def _onchange_set_price_lines(self):
        if self.set_price_lines:
            self.order_line.update({"set_price": self.set_price_lines})
        else:
            self.order_line.update({"set_price": ""})

    def action_confirm(self):
        lines_wo_set_price = self.order_line.filtered(lambda x: not x.set_price)
        if lines_wo_set_price:
            raise ValidationError(
                _("There's at least one line without 'set price' field filled, please check")
            )
        super().action_confirm()
