# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models
from odoo.tools import float_is_zero, float_compare


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    qty_delivered_dest = fields.Float(
        "Destination Delivered Quantity",
        copy=False,
        compute="_compute_qty_delivered_dest",
        compute_sudo=True,
        store=True,
        readonly=True,
        digits="Product Unit of Measure",
        help="""
        This field shows the delivered quantity accepted by destination.
        Depending on invoice policy, this field could be used for invoicing
        purposes
        """,
        default=0.0,
    )
    product_invoice_policy = fields.Selection(
        related="product_id.invoice_policy",
    )

    @api.depends(
        "move_ids.state",
        "move_ids.scrapped",
        "move_ids.qty_delivered_dest",
        "move_ids.product_uom",
    )
    def _compute_qty_delivered_dest(self):
        for line in self.filtered(
            lambda x: x.qty_delivered_method == "stock_move"
        ):
            qty = 0.0
            outgoing_moves, incoming_moves = line._get_outgoing_incoming_moves()
            for move in outgoing_moves.filtered(lambda x: x.state == "done"):
                qty += move.product_uom._compute_quantity(move.qty_delivered_dest, line.product_uom, rounding_method='HALF-UP')
            for move in incoming_moves.filtered(lambda x: x.state == "done"):
                qty -= move.product_uom._compute_quantity(move.qty_delivered_dest, line.product_uom, rounding_method='HALF-UP')
            line.qty_delivered_dest = qty

    @api.depends("qty_delivered_dest")
    def _get_to_invoice_qty(self):
        """
        qty_to_invoice attends the new possible invoice policy
        """
        super()._get_to_invoice_qty()
        for line in self.filtered(
            lambda x: x.state in ("sale", "done")
            and x.product_id.invoice_policy == "stock_move_dest"
        ):
            line.qty_to_invoice = line.qty_delivered_dest - line.qty_invoiced

    @api.depends("qty_delivered_dest")
    def _compute_invoice_status(self):
        super()._compute_invoice_status()
        precision = self.env['decimal.precision'].precision_get(
            "Product Unit of Measure"
        )
        for line in self.filtered(
            lambda x: x.state in ("sale", "done")
            and x.product_id.invoice_policy == "stock_move_dest"
        ):
            if not float_is_zero(line.qty_to_invoice, precision_digits=precision):
                line.invoice_status = 'to invoice'
            elif float_is_zero(
                line.qty_delivered_dest, precision_digits=precision
            ):
                # Only when qty_delivered_dest is > 0 we're able to check if
                #  it's invoiced
                line.invoice_status = "no"
            elif float_compare(
                line.qty_invoiced, line.qty_delivered_dest, precision_digits=precision
            ) >= 0:
                line.invoice_status = "invoiced"
            else:
                # TODO is this case possible?
                line.invoice_status = "no"
