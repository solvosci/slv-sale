# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_update_prices(self):
        return super(SaleOrder, self.with_context(not_change_prices_from_pricelist=True)).action_update_prices()
