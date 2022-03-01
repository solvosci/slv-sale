# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    picking_first_date = fields.Datetime(
        compute="_compute_picking_first_date",
        store=True,
        help="""
        Shows, for the done pickings where this line was involved,
        the first done date
        """,
    )
    invoice_first_date = fields.Date(
        compute="_compute_invoice_first_date",
        help="""
        Shows, for the invoice where this line was involved,
        the first invoice date
        """,
    )

    @api.depends("move_ids.state")
    def _compute_picking_first_date(self):
        for line in self:
            moves = line.move_ids.filtered(
                lambda x: x.state == "done"
            )
            line.picking_first_date = (
                moves and moves.sorted("date")[0].date
                or False
            )

    def _compute_invoice_first_date(self):
        for line in self:
            moves = line.invoice_lines.filtered(
                lambda x: x.move_id.invoice_date
            ).mapped("move_id")
            line.invoice_first_date = (
                moves and moves.sorted("invoice_date")[0].invoice_date
                or False
            )
