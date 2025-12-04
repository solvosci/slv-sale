# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, fields, api
from .res_partner import INVOICE_PERIOD_SELECTION

class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_invoice_period = fields.Selection(
        selection=INVOICE_PERIOD_SELECTION,
        compute='_compute_partner_invoice_period',
        string="Invoice Period",
        store=True,
        readonly=False,
    )

    @api.depends('partner_id.invoice_period','partner_id.parent_id.invoice_period')
    def _compute_partner_invoice_period(self):
        for order in self.filtered(lambda o: o.state in ('draft', 'sent')):
            order.partner_invoice_period = (
                order.partner_id.invoice_period
                or
                order.partner_id.parent_id.invoice_period
            )
