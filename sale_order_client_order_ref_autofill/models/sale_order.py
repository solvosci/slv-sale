# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    client_order_ref = fields.Char(string="Work Number")
    client_order_ref_mandatory = fields.Boolean(related="type_id.client_order_ref_mandatory")

    def action_confirm(self):
        res = super().action_confirm()
        if self.type_id and self.client_order_ref_mandatory:
            self.client_order_ref = self.env['ir.sequence'].next_by_code('sale.order.work.number')
        return res
