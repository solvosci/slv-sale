# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class SaleOrderLine(models.Model):
    _name = "sale.order.line"
    _inherit = ["sale.order.line", "color.tintometric.system.mixin"]
