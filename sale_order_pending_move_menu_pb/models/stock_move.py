# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    move_product_brand_id = fields.Many2one("product.brand", related="product_id.product_brand_id", string="Brand", help="", store=True)
