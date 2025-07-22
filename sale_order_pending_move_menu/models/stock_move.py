# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = "stock.move"

    move_sale_order_id = fields.Many2one("sale.order", related="sale_line_id.order_id", store=True, string="Sale Order")
    move_date_order = fields.Datetime(related="picking_id.sale_id.date_order", store=True)
    move_partner_id = fields.Many2one("res.partner", related="picking_id.sale_id.partner_id", store=True, string="Customer")
    move_product_uom_qty_sale = fields.Float(related="sale_line_id.product_uom_qty")
    move_product_uom_sale = fields.Many2one("uom.uom", related='sale_line_id.product_uom')
    picking_state = fields.Selection(related="picking_id.state")
    move_warehouse_id = fields.Many2one(related="sale_line_id.warehouse_id")
    move_user_id = fields.Many2one(related="move_sale_order_id.user_id", store=True)
