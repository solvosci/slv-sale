# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("move_ids.state")
    def _compute_analytic_tag_ids(self):
        # Assign the analytic tag on the sales order line based on first
        #  done move location warehouse.
        # If location is the default stock location of certain warehouse,
        #  it will be use with priority; otherwise, the warhouse location itself        
        super()._compute_analytic_tag_ids()
        warehouse_ids = self.env["stock.warehouse"].search([])
        for line in self:
            move_ids = line.move_ids.filtered(lambda x: x.state == "done")
            if move_ids:
                # We'll find at least one move line, so it's secure
                location = move_ids.move_line_ids.location_id[0]
                # TODO we assume a few warehouses, so this is very fast
                warehouse = warehouse_ids.filtered(lambda x: x.lot_stock_id == location)
                if not warehouse:                    
                    warehouse = location.get_warehouse()
                if warehouse:
                    line.analytic_tag_ids = warehouse[0].account_analytic_tag_ids
