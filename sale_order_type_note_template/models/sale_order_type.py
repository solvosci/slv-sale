# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import fields, models


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    terms_template_id = fields.Many2one(
        comodel_name="sale.terms_template",
        help="Default Terms and conditions Template applied to orders"
        " for the selected type",
    )
