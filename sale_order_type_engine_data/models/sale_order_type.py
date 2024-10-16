# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class SaleOrderType(models.Model):
    _inherit = 'sale.order.type'

    engine_data_enabled = fields.Boolean(default=False)
