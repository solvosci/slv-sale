# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    invoice_policy = fields.Selection(
        selection_add=[("stock_move_dest", "Stock Moves - Destination Quantity")],
        default="stock_move_dest",
    )
