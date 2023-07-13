# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    sale_standard_total_taxes = fields.Boolean(string='Standard Subtotal Taxes')
