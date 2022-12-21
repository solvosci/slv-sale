# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_sale_order_confirm_multi(self):
        for record in self.browse(self.env.context['active_ids']).filtered(lambda x: x.state in ('draft', 'sent')):
            record.action_confirm()
