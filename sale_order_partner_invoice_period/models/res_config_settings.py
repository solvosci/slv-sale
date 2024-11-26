# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models
from .res_partner import INVOICE_PERIOD_SELECTION

class ResCompany(models.Model):
    _inherit = "res.company"

    invoice_period_default = fields.Selection(INVOICE_PERIOD_SELECTION)
    
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    invoice_period_default = fields.Selection(
        selection=INVOICE_PERIOD_SELECTION,
        related='company_id.invoice_period_default',
        help="Select default invoice period for new companys",
        readonly=False
        )
    