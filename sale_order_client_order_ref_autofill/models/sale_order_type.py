# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    client_order_ref_mandatory = fields.Boolean(string="Work Number Mandatory")

