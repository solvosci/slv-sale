# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models
from odoo.tools import float_compare


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _action_launch_stock_rule(self, previous_product_uom_qty=False):
        lines_sn = self.filtered(
            lambda x: x.product_id.tracking == "serial"
        )
        if lines_sn:
            precision = self.env["decimal.precision"].precision_get("Product Unit of Measure")
        for line in lines_sn:
            times = int(
                line.product_uom_qty
                -
                line._get_qty_procurement(
                    previous_product_uom_qty=previous_product_uom_qty
                )
                -
                (
                    previous_product_uom_qty
                    and previous_product_uom_qty.get(line.id, 0.0)
                    or 0.0
                )
            )
            line = line.with_context(
                sale_stock_sn_single=True,
                sale_stock_sn_single_precision=precision,
            )
            for k in range(0, times):
                moves_prev = line.move_ids
                super(SaleOrderLine, line)._action_launch_stock_rule(
                    previous_product_uom_qty=previous_product_uom_qty
                )
                new_move = line.move_ids - moves_prev
                # This ensures that move lines are splitted and not merged, as
                #  description_picking is one of the fields covered by
                #  _prepare_merge_moves_distinct_fields()
                # TODO replace by a specific new "sequence within same product" field
                new_move.description_picking = "%s #%d" % (new_move.description_picking, k+1)
        super(SaleOrderLine, self - lines_sn)._action_launch_stock_rule(
            previous_product_uom_qty=previous_product_uom_qty
        )
        return True

    def _get_qty_procurement(self, previous_product_uom_qty=False):
        """
        When we come from special lauch rule for S/N tracked products,
        we ensure that we'll procure 1 quantity
        """
        qty = super()._get_qty_procurement(
            previous_product_uom_qty=previous_product_uom_qty
        )
        # TODO previous_product_uom_qty management (in case of qty update on sale order line)
        if self.env.context.get("sale_stock_sn_single", False):
            if float_compare(
                qty,
                self.product_uom_qty,
                precision_digits=self.env.context.get("sale_stock_sn_single_precision", 0.001)
            ) < 0:
                qty = self.product_uom_qty - 1.0
        return qty
