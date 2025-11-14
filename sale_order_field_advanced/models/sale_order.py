# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields
from odoo.http import request


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    adv_requested_delivery_date = fields.Date(string='Requested Delivery Date')

    def complement_size(self, line):
        product_values = line.product_id.product_template_attribute_value_ids.mapped("product_attribute_value_id")
        if product_values:
            equivalence = request.env["product.complement.size"].sudo().search([
                ("product_size_ids", "in", product_values.ids),
                ("active", "=", True)
            ], limit=1)
            line.adv_complement_size = equivalence.name
            if line.adv_complement_id and equivalence:
                line.adv_complement_group = f"{line.adv_complement_id.name} | {equivalence.name}".strip()
