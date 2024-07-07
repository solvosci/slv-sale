# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models
from odoo.tools import float_compare


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    def explode(self, product, quantity, picking_type=False):
        """
        Split BoM lines for tracking serial products, when qty=N (> 1),
        into N BoM lines with qty=1, when needed 
        """
        boms_done, lines_done = super().explode(product, quantity, picking_type=picking_type)
        if not self.env.context.get("kit_sn_single", False):
            return boms_done, lines_done
        new_lines_done = []
        for line_done in lines_done:
            bom_line_id = line_done[0]
            values = line_done[1]
            int_qty = int(values.get("qty"))
            if (
                bom_line_id.product_id.tracking != "serial"
                or (
                    bom_line_id.product_id.tracking == "serial"
                    and int_qty == 1
                )
            ):
                new_lines_done.append(line_done)
            else:
                new_values = values.copy()
                new_values["qty"] = 1
                for k in range(0, int_qty):
                    new_lines_done.append((bom_line_id, new_values))
        return boms_done, new_lines_done
