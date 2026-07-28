# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    batch_ids =  fields.Many2many('stock.picking.batch', compute='_compute_batch_ids', store=True)

    @api.depends('move_ids.picking_id.batch_id')
    def _compute_batch_ids(self):
        for record in self:
            record.batch_ids = record.move_ids.picking_id.batch_id
