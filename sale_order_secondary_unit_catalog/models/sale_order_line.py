# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_product_catalog_lines_data(self, **kwargs):
        res = super()._get_product_catalog_lines_data(**kwargs)
        # For the target product, if it has a secondary unit, we need to
        #  convert quantity; if not, we'll accept the default behavior (manage
        #  the catalog with main unit), no matter if line has already second
        #  unit info
        if self.product_id.sale_secondary_uom_id:
            # TODO Assumtions:
            # * If destination unit is integer (like e.g. units), rounding it is not necessary
            if len(self) == 1:
                res["quantity"] = self.secondary_uom_qty
            elif len(self) > 1:
                # TODO if line.secondary_uom_id and/or sale_secondary_uom_id are not defined?
                res["quantity"] = sum(
                    line.secondary_uom_id._compute_quantity(
                        qty=line.secondary_uom_qty,
                        to_unit=line.product_id.sale_secondary_uom_id,
                    )
                    for line in self.filtered(lambda line: line.secondary_uom_id)
                )
        return res
