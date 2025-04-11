# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    has_process_control = fields.Boolean(default=False)
