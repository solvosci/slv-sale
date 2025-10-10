# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    move_delivery_status = fields.Selection(related="move_sale_order_id.delivery_status", string="Delivery status")
