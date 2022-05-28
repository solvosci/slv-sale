# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def write(self, values):
        """
        When state changes, for a sale order (not quotation)
        we only keep alive those projects that belong to non locked
        neither cancelled order.
        """
        res = super().write(values)
        new_state = values.get("state")
        if new_state and new_state in ["sale", "done", "cancel"]:
            active = (new_state == "sale")
            # We're only interested in line related projects,
            #  so we exclude product and sales order ones, provided by
            #  project_ids
            projects = self.sudo().with_context(
                active_test=False
            ).mapped("order_line.project_id")
            if projects:
                projects.write({"active": active})
        return res
