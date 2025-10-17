# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    complement_category_ids = fields.Many2many(
        'product.category',
        'product_category_complement_rel',
        'complement_id',
        'category_id',
        string='Complement Categories',
        domain=[('is_complement_category', '=', True)]
    )
