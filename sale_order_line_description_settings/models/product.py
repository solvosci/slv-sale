# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models

# sale_order_line_description_settings

class ProductProduct(models.Model):
    _inherit = "product.product"

    def get_product_multiline_description_sale(self):
        super().get_product_multiline_description_sale()

        if not self.env.company.product_default_code_hidden:
            name = self.display_name
        else:
            name = self.name

        if self.description_sale:
            if not self.env.company.product_inline_description_sale:
                name += '\n%s' % (self.description_sale)
            else:
                name += ' %s' % (self.description_sale)
        return name
