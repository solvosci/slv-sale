# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, api


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
