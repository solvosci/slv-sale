# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    sale_secondary_uom_id = fields.Many2one(
        comodel_name="product.secondary.unit",
        string="Default secondary unit for sales",
    )
