# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    menu_invoice_first_date = fields.Date(
        string="First Invoice Date",
        compute="_compute_menu_invoice_first_date",
        help="""
        Shows, for the invoices where this move was involved,
        the first invoice date
        """,
    )

    def _compute_menu_invoice_first_date(self):
        for move in self:
            invoices = move.invoice_line_ids.mapped("move_id").filtered(
                lambda x: x.invoice_date
            )
            move.menu_invoice_first_date = (
                invoices and invoices.sorted("invoice_date")[0].invoice_date
                or False
            )
