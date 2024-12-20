# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    color_code_tintometric = fields.Char(compute="_compute_color_code_tintometric", string="Lot/S.Tin")

    @api.depends('sale_line_ids.color_code_tintometric')
    def _compute_color_code_tintometric(self):
        for record in self:
            record.color_code_tintometric = ", ".join(record.sale_line_ids.filtered(lambda x: x.color_code_tintometric).mapped("color_code_tintometric"))
