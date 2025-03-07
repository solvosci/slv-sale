# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_partner_editor = fields.Boolean(
            compute="_compute_is_partner_editor"
        )

    @api.depends()
    def _compute_is_partner_editor(self):
        for record in self:
            record.is_partner_editor = self.env.user.has_group('partner_readonly_security.group_partner_edition')
