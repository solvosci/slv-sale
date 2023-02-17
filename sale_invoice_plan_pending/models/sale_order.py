# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    invoice_plan_pending = fields.Integer(
        compute="_compute_invoice_plan_pending",
        string="Pending plans",
        store= True,
    )

    @api.depends("invoice_plan_ids.invoiced")
    def _compute_invoice_plan_pending(self):
        for order in self:
            order.invoice_plan_pending = len(
                order.invoice_plan_ids.filtered(lambda x: not x.invoiced)
            )
