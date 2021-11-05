# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    task_id = fields.Many2one(related="move_id.sale_line_id.task_id")
