# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models
from odoo.tools import float_is_zero


class SaleOrder(models.Model):
    _inherit = "sale.order"

    has_pend_qty_delivered_dest = fields.Boolean(
        string="Has Pending Destination Delivered Quantity",
        compute="_compute_has_pend_qty_delivered_dest",
        store=True,
        help="""
        Indicates if any done stock move linked to this order has
        destination delivered quantity not filled yet
        """,
    )

    @api.depends(
        "picking_ids.move_lines.state",
        "picking_ids.move_lines.qty_delivered_dest",
    )
    def _compute_has_pend_qty_delivered_dest(self):
        for order in self:
            moves_done = order.picking_ids.move_lines.filtered(
                lambda x: x.state == "done"
                and x.product_id.invoice_policy == "stock_move_dest"
            )
            if moves_done:
                order.has_pend_qty_delivered_dest = any(
                    float_is_zero(
                        move.qty_delivered_dest,
                        precision_rounding=move.product_id.uom_id.rounding
                    ) for move in moves_done
                )
            else:
                order.has_pend_qty_delivered_dest = False
