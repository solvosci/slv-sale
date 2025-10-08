# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class SaleOrderLineProcessStatus(models.Model):
    _name = 'sale.order.line.process.status'
    _description = 'Sale Order Line Process Status'
    _order = 'sequence'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()
    active = fields.Boolean(default=True)
    initial_default_state = fields.Boolean(string='Is Initial State', default=False)
    no_process_default_state = fields.Boolean(string='Is Initial No Process State', default=False)
    final_state = fields.Boolean(default=False)
    decoration_color = fields.Selection([
        ('muted', 'Grey'),
        ('warning', 'Yellow'),
        ('success', 'Green'),
        ('danger', 'Red'),
        ('info', 'Blue'),
    ])
