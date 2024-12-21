# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    def _onchange_helper_product_uom_for_secondary(self):
        """
        For special case when a line is initialized, value 1.0 is set for main
        product qty. In that case, we set such value for secondary unit instead
        """
        super()._onchange_helper_product_uom_for_secondary()
        line_qty = self._get_quantity_from_line()
        if (
            line_qty == 1.0
            and self.secondary_uom_qty
            and self.secondary_uom_id.dependency_type != "independent"
        ):
            self.secondary_uom_qty = 1.0
