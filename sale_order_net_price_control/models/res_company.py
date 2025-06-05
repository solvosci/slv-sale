# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    lowest_pricelist_id = fields.Many2one(comodel_name='product.pricelist', string='Pricelist')
