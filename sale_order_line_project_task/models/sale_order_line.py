# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_type = fields.Selection(related="product_id.type")
    tasks_ids = fields.Many2many(related="order_id.tasks_ids")
