# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _get_aggregated_properties(self, move_line=False, move=False):
        result = super()._get_aggregated_properties(move_line=move_line, move=move)
        move = result['move']
        if move.sale_line_id:
            sale_line_id = move.sale_line_id.id
        else:
            sale_line_id = 0
        result['line_key'] = f"{result['line_key']}_{sale_line_id}"
        return result
