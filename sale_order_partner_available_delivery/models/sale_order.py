# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _compute_partner_invoice_id(self):
        super()._compute_partner_invoice_id()
        for order in self:
            order.partner_invoice_id = order.partner_id
