# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _notify_get_reply_to(self, default=None):
        res = super()._notify_get_reply_to(default=default)
        forced = self.env['ir.config_parameter'].sudo().get_param('sale.reply_to_email')
        if not forced:
            return res
        for so in self:
            res[so.id] = self._notify_get_reply_to_formatted_email(
                forced,
                so.display_name or '',
                company=so.company_id
            )
        return res
