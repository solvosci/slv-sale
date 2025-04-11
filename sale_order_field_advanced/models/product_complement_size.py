from odoo import models, fields

class ProductComplementSize(models.Model):
    _name = 'product.complement.size'
    _description = 'Product Complement Size'

    name = fields.Char(string="Complement Size", required=True)
    active = fields.Boolean(default=True)
    attribute_id = fields.Many2one('product.attribute', required=True)
    product_size_ids = fields.Many2many(
            'product.attribute.value',
            required=True,
            domain="[('attribute_id', '=', attribute_id)]"
        )
