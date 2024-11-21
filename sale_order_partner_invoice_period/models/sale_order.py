# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_invoice_period = fields.Selection(
        selection=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('fortnightly', 'Fortnightly'),
            ('monthly', 'Monthly'),
            ('quarterly', 'Quarterly'),
            ('yearly', 'Yearly'),
        ],
        compute='_compute_partner_invoice_period',
        string="Invoice Period",
        store=True
    )

    @api.depends('partner_invoice_id.invoice_period', 'partner_invoice_id.parent_id.invoice_period')
    def _compute_partner_invoice_period(self):
        for order in self:
            if order.partner_invoice_id:
                if order.partner_invoice_id.invoice_period:
                    order.partner_invoice_period = order.partner_invoice_id.invoice_period
                elif (
                    order.partner_invoice_id.parent_id
                    and order.partner_invoice_id.parent_id.invoice_period):
                    order.partner_invoice_period = order.partner_invoice_id.parent_id.invoice_period
                else:
                    order.partner_invoice_period = False 
            else:
                order.partner_invoice_period = False 
