# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, api, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends('product_id', 'company_id', 'currency_id', 'product_uom', 'lot_id')
    def _compute_purchase_price(self):
        super(SaleOrderLine, self)._compute_purchase_price()
        for line in self:
            if line.lot_id.fcd_origin_lot_id:
                line.purchase_price = line.lot_id.fcd_origin_lot_id.fcd_document_line_id.price_real_kg
            elif line.lot_id.fcd_document_line_id:
                line.purchase_price = line.lot_id.fcd_document_line_id.price_real_kg

    def action_open_stock_quant(self):
        # self.ensure_one()
        # action = self.env.ref("stock.dashboard_open_quants").read()[0]
        # action["context"] = {
        #     "search_default_product_id": self.product_id.id,
        #     "group_by": ["lot_id"],
        # }
        # return action

        self.ensure_one()
        stock_quant_ids = self.env['stock.quant'].search([])

        return {
            'name': _('Stock Quant'),
            'res_model': 'stock.quant',
            'view_mode': 'tree',
            'view_type': 'tree',
            'res_id': stock_quant_ids.ids,
            'target': 'new',
            'type': 'ir.actions.act_window',
            'domain': [('location_id.usage','=', 'internal')],
            'context': {
                "search_default_product_id": self.product_id.id,
                # "group_by": ["lot_id"],
            }
        }
