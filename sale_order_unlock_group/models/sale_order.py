# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        res = super().action_confirm()
        if self.env.user.has_group(
            "sale_order_unlock_group.group_auto_done_disable_setting"
        ):
            self.action_unlock()
        return res
