# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def get_delivered_order(self):
        # Force caching lines and line taxes
        self.mapped("order_line.tax_id")
        so_vals = self._convert_to_write(self._cache)
        valued_order = self.new(so_vals)
        for line_org, line_dest in zip(self.order_line, valued_order.order_line):
            line_dest.product_uom_qty = line_org.qty_delivered
        return valued_order
