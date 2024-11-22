# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, fields

INVOICE_PERIOD_SELECTION = [
    ('daily','Daily'),
    ('weekly','Weekly'),
    ('fortnightly','Fortnightly'),
    ('monthly','Monthly'),
    ('quarterly','Quarterly'),
    ('yearly','Yearly')
]


class ResPartner(models.Model):
    _inherit = "res.partner"

    invoice_period = fields.Selection(INVOICE_PERIOD_SELECTION)
