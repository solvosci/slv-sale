# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    note = fields.Char()
