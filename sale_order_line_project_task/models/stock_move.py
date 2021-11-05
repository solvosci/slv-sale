# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    task_id = fields.Many2one(related="sale_line_id.task_id")
