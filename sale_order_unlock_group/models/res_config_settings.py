# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_auto_done_disable_setting_sale_order = fields.Boolean(
        string="Lock Confirmed Sales- Make initially unlocked",
        implied_group='sale_order_unlock_group.group_auto_done_disable_setting',
    )

    group_auto_done_disable_setting_invoice = fields.Boolean(
        string="Lock Confirmed Sales- Automatically when invoiced",
        implied_group='sale_order_unlock_group.group_auto_done_disable_setting_invoice',
    )

    @api.onchange("group_auto_done_setting")
    def _onchange_group_auto_done_setting(self):
        if not self.group_auto_done_setting:
            self.group_auto_done_disable_setting_sale_order = False
            self.group_auto_done_disable_setting_invoice = False
