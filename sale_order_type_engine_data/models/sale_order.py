# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    engine_data_enabled = fields.Boolean(related="type_id.engine_data_enabled")
