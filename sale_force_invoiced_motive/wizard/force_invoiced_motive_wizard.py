# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import fields, models
from ..models.sale_order import FORCE_INVOICED_MOTIVES


class ForceInvoicedMotive(models.TransientModel):
    _name = "force.invoiced.motive.wizard"

    sale_order_ids = fields.Many2many('sale.order')
    motive = fields.Selection(FORCE_INVOICED_MOTIVES)

    def action_save_motive(self):
        for record in self:
            for sale_order in record.sale_order_ids:
                sale_order.forced_invoice_motive = record.motive
