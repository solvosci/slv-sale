# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def copy_sol(self):
        for line in self:
            if line.order_id.state == "cancel" or line.order_id.locked:
                raise UserError(_("You cannot copy lines from a canceled or locked sale order."))
            line.copy(default={'order_id': line.order_id.id})
