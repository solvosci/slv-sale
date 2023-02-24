# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if self.env.user.has_group(
            "sale_order_unlock_group.group_auto_done_disable_setting_invoice"
        ):
            res.invoice_line_ids.sale_line_ids.order_id.filtered(
                lambda x: x.state != "done"
            ).action_done()
        return res
