# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, _, api


class FCDStockQuant(models.TransientModel):
    _name = 'fcd.stock.quant.wizard'
    _description = 'fcd.stock.quant.wizard'

    stock_quant_id = fields.Many2one('stock.quant')
    sale_line_id = fields.Many2one('sale.order.line')

    location_id = fields.Many2one(related='stock_quant_id.location_id')
    lot_id = fields.Many2one(related='stock_quant_id.lot_id')
    inventory_quantity = fields.Float(related='stock_quant_id.inventory_quantity')
    available_quantity = fields.Float(related='stock_quant_id.available_quantity')
    currency_id = fields.Many2one(related='stock_quant_id.currency_id')
    value = fields.Monetary(related='stock_quant_id.value')

    purchase_price = fields.Float(string='Cost', compute='_compute_purchase_price')

    def _compute_purchase_price(self):
        for record in self:
            if record.lot_id.fcd_origin_lot_id:
                record.purchase_price = record.lot_id.fcd_origin_lot_id.fcd_document_line_id.price_real_kg
            elif record.lot_id.fcd_document_line_id:
                record.purchase_price = record.lot_id.fcd_document_line_id.price_real_kg
            else:
                record.purchase_price = False

    def action_select_lot(self):
        self.sale_line_id.lot_id = self.lot_id.id
