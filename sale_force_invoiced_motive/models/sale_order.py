# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, fields, api

FORCE_INVOICED_MOTIVES = [
    ('advance', 'Advance'),
    ('deposit', 'Deposit'),
    ('completed/invoiced', 'Completed/Invoiced'),
    ('others', 'Others')
]

class SaleOrder(models.Model):
    _inherit = "sale.order"

    force_invoiced_motive = fields.Selection(FORCE_INVOICED_MOTIVES)

    @api.depends('force_invoiced')
    def _compute_invoice_status(self):
        res = super()._compute_invoice_status()
        if not self.force_invoiced:
            self.force_invoiced_motive = False
        return res

    # def action_force_invoiced(self):
    #     for record in self:
    #         record.force_invoiced=True
    #     res = self._compute_invoice_status()
    #     return res
    
    def action_force_invoiced(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Force Invoiced'),
                'res_model': 'force.invoiced.motive.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_sale_order_ids': self.ids}, }
    