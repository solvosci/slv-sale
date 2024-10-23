# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("move_ids.state")
    def _compute_analytic_tag_ids(self):
        super()._compute_analytic_tag_ids()
        for line in self:
            move_ids = line.move_ids.filtered(lambda x: x.state == "done")
            if move_ids:
                warehouse_id = move_ids.move_line_ids.location_id.get_warehouse()
                if warehouse_id:
                    line.analytic_tag_ids = warehouse_id.account_analytic_tag_ids
