# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    product_categ_id = fields.Many2one(related='product_id.categ_id')
    sale_order = fields.Many2one(related='sale_line_id.order_id', store=True)
    sale_partner_id = fields.Many2one(
        related='sale_order.partner_id',
        store=True
    )
    sale_user_id = fields.Many2one(related="sale_line_id.order_id.user_id")
