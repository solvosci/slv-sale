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
        self.ensure_one()
        stock_quant_ids = self.env['stock.quant'].search([
            ('location_id.usage','=', 'internal'),
            ('product_id', '=', self.product_id.id)
        ])

        wizard_ids = self.env['fcd.stock.quant.wizard']
        for record in stock_quant_ids:
            wizard_ids += self.env['fcd.stock.quant.wizard'].create({
                'stock_quant_id': record.id,
                'sale_line_id': self.id,
            })

        return {
            'name': _('Stock Quant'),
            'res_model': 'fcd.stock.quant.wizard',
            'view_mode': 'list',
            'view_type': 'list',
            'domain': [('id', 'in', wizard_ids.ids)],
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
