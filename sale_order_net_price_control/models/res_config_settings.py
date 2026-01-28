# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lowest_pricelist_id = fields.Many2one(related="company_id.lowest_pricelist_id", readonly=False, string='Pricelist')
