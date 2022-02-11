# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    amount_to_invoice = fields.Monetary(
        string="To Invoice",
        store=True,
        readonly=True,
        compute="_compute_amount_to_invoice",
        help="Total amount currently pending to invoice (tax excl.)",
    )

    @api.depends("order_line.qty_to_invoice", "order_line.price_unit_wd")
    def _compute_amount_to_invoice(self):
        for order in self:
            order.amount_to_invoice = sum([
                line.qty_to_invoice * line.price_unit_wd
                for line in order.order_line
            ])
