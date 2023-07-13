# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_standard_total_taxes = fields.Boolean(related='company_id.sale_standard_total_taxes', string="Standard Subtotal Taxes", readonly=False)
