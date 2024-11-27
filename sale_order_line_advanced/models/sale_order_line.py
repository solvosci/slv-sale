# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    date_order = fields.Datetime(related='order_id.date_order', store=True)
    last_update_order = fields.Datetime(related='order_id.write_date', store=True)
