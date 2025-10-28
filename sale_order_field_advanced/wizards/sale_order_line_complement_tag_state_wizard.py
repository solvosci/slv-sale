# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class SaleOrderLineComplementTagStateWizard(models.TransientModel):
    _name = 'sale.order.line.complement.tag.wizard'
    _description = 'Change Complement And Tag State Wizard'
    _inherit = 'adv.state.mixin'

    line_ids = fields.Many2many('sale.order.line', string='Sale Order Lines')

    change_tag_state = fields.Boolean(string="Change Tag State", default=True)
    change_complement_state = fields.Boolean(string="Change Complement State", default=True)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        lines = self.env['sale.order.line'].browse(self.env.context.get('active_ids', []))
        if lines:
            tag_values = lines.mapped('adv_tag_state')
            complement_values = lines.mapped('adv_complement_state')

            if len(set(tag_values)) == 1:
                res['adv_tag_state'] = tag_values[0]
            if len(set(complement_values)) == 1:
                res['adv_complement_state'] = complement_values[0]

            res['line_ids'] = [(6, 0, lines.ids)]
        return res

    def change_complement_and_tag_state(self):
        if not self.line_ids:
            self.line_ids = self.env['sale.order.line'].browse(self.env.context.get('active_ids', []))
        if not self.line_ids:
            return

        vals = {}
        if self.change_tag_state:
            vals['adv_tag_state'] = self.adv_tag_state
        if self.change_complement_state:
            vals['adv_complement_state'] = self.adv_complement_state

        if vals:
            self.line_ids.write(vals)
