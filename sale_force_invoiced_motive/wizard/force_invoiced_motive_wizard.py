# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models, _
from odoo.exceptions import ValidationError
from ..models.sale_order import FORCE_INVOICED_MOTIVES


class ForceInvoicedMotive(models.TransientModel):
    _name = "force.invoiced.motive.wizard"
    _description = "Add forced invoiced motives"

    sale_order_ids = fields.Many2many('sale.order')
    motive = fields.Selection(FORCE_INVOICED_MOTIVES)

    def action_save_motive(self):
        if self.motive:
            for sale_order in self.sale_order_ids:
                sale_order.force_invoiced_motive = self.motive
                sale_order.force_invoiced = True
                sale_order._compute_invoice_status()
        else:
            raise ValidationError(_("The motive can´t be empty"))
