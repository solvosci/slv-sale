# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models
from odoo.tools import float_is_zero


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def get_stock_moves_link_invoice(self):
        moves = super().get_stock_moves_link_invoice()
        return moves.filtered(
            lambda mv: not (
                mv.product_id.invoice_policy == "stock_move_dest"
                and float_is_zero(
                    mv.qty_delivered_dest,
                    precision_rounding=mv.product_id.uom_id.rounding
                )
            )
        )
