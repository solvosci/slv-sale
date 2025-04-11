# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class SaleOrderLineManufacturingStateWizard(models.TransientModel):
    _name = 'sale.order.line.manufacturing.state.wizard'
    _description = 'Change Manufacturing State Wizard'

    line_ids = fields.Many2many('sale.order.line', string='Sale Order Lines')

    adv_manufacturing_state_id = fields.Many2one('sale.order.line.process.status')

    def change_manufacturing_state(self):
        self.line_ids.adv_manufacturing_state_id=  self.adv_manufacturing_state_id
