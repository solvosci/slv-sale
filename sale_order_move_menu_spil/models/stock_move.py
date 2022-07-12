# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import fields, models, api
from odoo.tools import float_compare


class StockMove(models.Model):
    _inherit = "stock.move"

    menu_invoice_first_date = fields.Date(
        string="Sale First Invoice Date",
        compute="_compute_sale_move_menu",
        store=True,
        help="""
        Shows, for the invoices where this move was involved,
        the first invoice date
        """,
    )

    currency_id = fields.Many2one(related='sale_line_id.currency_id')

    menu_price_unit = fields.Float(
        compute="_compute_sale_move_menu",
        string="Unit Price",
        store=True
    )
    menu_quantity_done = fields.Float(
        compute="_compute_sale_move_menu",
        string="Quantity",
        digits="Product Unit of Measure",
        store=True
    )
    menu_price_amount_total = fields.Monetary(
        compute="_compute_sale_move_menu",
        string="Amount Total",
        store=True,
    )
    menu_invoice_lines_count = fields.Integer(
        compute="_compute_sale_move_menu",
        store=True
    )
    menu_negative_amount = fields.Boolean(
        compute="_compute_sale_move_menu",
        store=True
    )

    @api.depends("state", "sale_line_id.price_unit", "invoice_line_ids.move_id.state", "invoice_line_ids.price_unit", "quantity_done")
    def _compute_sale_move_menu(self):
        precision = self.env["decimal.precision"].precision_get("Product Price")
        for record in self:

            invoices = record.invoice_line_ids.mapped("move_id").filtered(
                lambda x: x.invoice_date
            )
            record.menu_invoice_first_date = (
                invoices and invoices.sorted("invoice_date")[0].invoice_date
                or False
            )

            invoice_lines = record.invoice_line_ids.filtered(lambda x: x.move_id.state == 'posted')
            record.menu_invoice_lines_count = len(invoice_lines)
            prices = [invoice.price_unit for invoice in invoice_lines]
            record.menu_quantity_done = record.quantity_done
            record.menu_negative_amount = False

            if any(1 if float_compare(prices[0], price, precision_digits=precision) else 0 for price in prices) or record.menu_invoice_lines_count == 0:
                record.menu_price_unit = record.sale_line_id.price_unit
            else:
                record.menu_price_unit = prices[0]
            record.menu_price_amount_total = record.menu_price_unit * record.quantity_done

            if record.picking_code == 'incoming':
                record.menu_quantity_done = -record.quantity_done
                record.menu_price_amount_total = -record.menu_price_amount_total
                record.menu_negative_amount = True
