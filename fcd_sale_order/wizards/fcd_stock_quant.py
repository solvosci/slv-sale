# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class FCDStockQuant(models.TransientModel):
    _name = 'fcd.stock.quant.wizard'
    _description = 'fcd.stock.quant.wizard'

    stock_quant_id = fields.Many2one('stock.quant')
    sale_line_id = fields.Many2one('sale.order.line')
    stock_move_line_id = fields.Many2one('stock.move.line')

    location_id = fields.Many2one(related='stock_quant_id.location_id')
    lot_id = fields.Many2one(related='stock_quant_id.lot_id')
    inventory_quantity = fields.Float(related='stock_quant_id.inventory_quantity')
    available_quantity = fields.Float(related='stock_quant_id.available_quantity')
    currency_id = fields.Many2one(related='stock_quant_id.currency_id')
    value = fields.Monetary(related='stock_quant_id.value')
    # secondary_uom_ids = fields.One2many(related='lot_id.secondary_uom_ids')

    inventory_quantity_secondary_uom = fields.Float(related='stock_quant_id.inventory_quantity_secondary_uom')
    product_stock_secondary_uom_id = fields.Many2one(related='stock_quant_id.product_stock_secondary_uom_id')

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
        # If open wizard from sale.order.line
        if self.sale_line_id:
            self.sale_line_id.write({
                "lot_id": self.lot_id.id,
                "lot_location_id": self.location_id.id,
            })
        # Else open wizard from stock.move.line
        else:
            self.stock_move_line_id.lot_id = self.lot_id.id
            self.stock_move_line_id.secondary_uom_qty = self.stock_move_line_id.move_id.secondary_uom_qty
            self.stock_move_line_id.qty_done = self.stock_move_line_id.move_id.product_uom_qty
            self.stock_move_line_id.location_id = self.location_id.id
            return self.stock_move_line_id.move_id.action_show_details()
