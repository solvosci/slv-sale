# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    task_id = fields.Many2one(related="sale_line_ids.task_id")
