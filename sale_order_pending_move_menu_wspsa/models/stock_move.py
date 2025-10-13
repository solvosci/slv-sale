# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    move_website_partner_ref = fields.Char(related="product_id.website_partner_ref", string="Partner reference")
