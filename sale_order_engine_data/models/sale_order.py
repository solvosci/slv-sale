# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    engine_ref = fields.Char(string="Engine number")
    engine_hours = fields.Integer(string="Engine hours")
