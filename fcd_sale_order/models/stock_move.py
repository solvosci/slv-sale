# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class StockMove(models.Model):
    _inherit = 'stock.move'

    def action_complete_stock_move_line(self):
        if self.purchase_line_id:
            super(StockMove, self).action_complete_stock_move_line()
        elif self.sale_line_id:
            values = {
                'move_id': self.id,
                'picking_id': self.picking_id.id,
                'company_id': self.company_id.id,
                'product_id': self.product_id.id,
                'product_uom_id': self.product_uom.id,
                'location_id': self.location_id.id,
                'location_dest_id': self.location_dest_id.id,
                'secondary_uom_id': self.sale_line_id.secondary_uom_id.id,
                'secondary_uom_qty': self.sale_line_id.secondary_uom_qty,
            }

            # Lot and Lines
            if self.move_line_ids and self.sale_line_id.lot_id:
                self.move_line_ids.unlink()
                values.update({
                    'lot_id': self.sale_line_id.lot_id.id,
                    "location_id": self.sale_line_id.lot_location_id.id,
                    'qty_done': self.product_uom_qty,
                })
            # Not Lot and Lines
            elif self.move_line_ids and not self.sale_line_id.lot_id:
                self.move_line_ids.unlink()
            # Lot and Not Lines
            elif not self.move_line_ids and self.sale_line_id.lot_id:
                values.update({
                    'lot_id': self.sale_line_id.lot_id.id,
                    "location_id": self.sale_line_id.lot_location_id.id,
                    'qty_done': self.product_uom_qty,
                })
            # Not Lot and Not Lines => nothing else
            elif not self.move_line_ids and not self.sale_line_id.lot_id:
                pass

            self.env['stock.move.line'].sudo().create(values)

            # # Lot and Lines
            # if self.move_line_ids and self.sale_line_id.lot_id:
            #     self.move_line_ids.unlink()
            #     self.env['stock.move.line'].sudo().create({
            #         'move_id': self.id,
            #         'company_id': self.company_id.id,
            #         'lot_id': self.sale_line_id.lot_id.id,
            #         'product_id': self.product_id.id,
            #         'product_uom_id': self.product_uom.id,
            #         'qty_done': self.product_uom_qty,
            #         'location_id': self.location_id.id,
            #         'location_dest_id': self.location_dest_id.id,
            #         'secondary_uom_id': self.sale_line_id.secondary_uom_id.id,
            #         'secondary_uom_qty': self.sale_line_id.secondary_uom_qty,
            #     })
            # # Not Lot and Lines
            # elif self.move_line_ids and not self.sale_line_id.lot_id:
            #     self.move_line_ids.unlink()
            #     self.env['stock.move.line'].sudo().create({
            #         'move_id': self.id,
            #         'company_id': self.company_id.id,
            #         'product_id': self.product_id.id,
            #         'product_uom_id': self.product_uom.id,
            #         'location_id': self.location_id.id,
            #         'location_dest_id': self.location_dest_id.id,
            #         'secondary_uom_id': self.sale_line_id.secondary_uom_id.id,
            #         'secondary_uom_qty': self.sale_line_id.secondary_uom_qty,
            #     })
            # # Lot and Not Lines
            # elif not self.move_line_ids and self.sale_line_id.lot_id:
            #     self.env['stock.move.line'].sudo().create({
            #         'move_id': self.id,
            #         'company_id': self.company_id.id,
            #         'lot_id': self.sale_line_id.lot_id.id,
            #         'product_id': self.product_id.id,
            #         'product_uom_id': self.product_uom.id,
            #         'qty_done': self.product_uom_qty,
            #         'location_id': self.location_id.id,
            #         'location_dest_id': self.location_dest_id.id,
            #         'secondary_uom_id': self.sale_line_id.secondary_uom_id.id,
            #         'secondary_uom_qty': self.sale_line_id.secondary_uom_qty,
            #     })
            # # Not Lot and Not Lines
            # elif not self.move_line_ids and not self.sale_line_id.lot_id:
            #     self.env['stock.move.line'].sudo().create({
            #         'move_id': self.id,
            #         'company_id': self.company_id.id,
            #         'product_id': self.product_id.id,
            #         'product_uom_id': self.product_uom.id,
            #         'location_id': self.location_id.id,
            #         'location_dest_id': self.location_dest_id.id,
            #         'secondary_uom_id': self.sale_line_id.secondary_uom_id.id,
            #         'secondary_uom_qty': self.sale_line_id.secondary_uom_qty,
            #     })
