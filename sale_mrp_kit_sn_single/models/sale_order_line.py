# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _action_launch_stock_rule(self, previous_product_uom_qty=False):
        """
        Alter current procedure only for kit products that have s/n product
        BoM lines
        """
        lines_kits_w_sn = self.browse()
        if self:
            bom_kits = self.env["mrp.bom"]._bom_find(
                self.product_id, company_id=self.company_id[0].id, bom_type="phantom"
            )
            for line in self:
                bom_id = bom_kits.get(line.product_id)
                if bom_id and bom_id.bom_line_ids.filtered(
                    lambda x: x.product_id.tracking == "serial"
                ):
                    lines_kits_w_sn |= line
        if lines_kits_w_sn:
            lines_kits_w_sn = lines_kits_w_sn.with_context(kit_sn_single=True)
            super(SaleOrderLine, lines_kits_w_sn)._action_launch_stock_rule(
                previous_product_uom_qty=previous_product_uom_qty
            )
        super(SaleOrderLine, self - lines_kits_w_sn)._action_launch_stock_rule(
            previous_product_uom_qty=previous_product_uom_qty
        )
