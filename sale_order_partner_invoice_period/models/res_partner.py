# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("invoice_period"):
                parent_id = vals.get("parent_id")
                parent = self.browse(parent_id)
                if parent.invoice_period:
                    vals["invoice_period"] = parent.invoice_period
                elif self.env.company.invoice_period_default:
                    vals["invoice_period"] = self.env.company.invoice_period_default
                else:
                    raise ValidationError(_("There is no default invoice period set.\nAdd an invoice period on partner or set one by default on:\nConfiguration > Sales > Accounting."))
        return super(ResPartner, self).create(vals_list)
