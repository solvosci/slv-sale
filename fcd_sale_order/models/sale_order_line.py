# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    lot_location_id = fields.Many2one(
        comodel_name="stock.location",
        help="""
        When a lot is selected from Stock Quant wizard, this field is filled
        with source location, that can be used in stock move line completion
        process
        """,
    )
    lot_product_unique = fields.Char(
        inverse='_set_lot_product_unique',
        help="""
        Technical field to help sales order imports select the correct lot
        using the lot name and product id in this format 'LOT00001 - 12345'
        """,
    )

    def _set_lot_product_unique(self):
        for record in self:
            data = record.lot_product_unique.split(' - ')
            if len(data) == 2:
                lot_name = data[0]
                product_id = data[1]
                lot_id = self.env['stock.production.lot'].search([('name', '=', lot_name), ('product_id.id', '=', product_id)])
                if lot_id:
                    record.lot_id = lot_id
                else:
                    raise ValidationError(
                        _("Lot not found for: {}".format(record.lot_product_unique))
                    )
            else:
                raise ValidationError(
                    _("Wrong format for: {}, should be like: 'LOT00001 - 12345'".format(record.lot_product_unique))
                )

    @api.depends('product_id', 'company_id', 'currency_id', 'product_uom', 'lot_id')
    def _compute_purchase_price(self):
        super(SaleOrderLine, self)._compute_purchase_price()
        for line in self:
            if line.lot_id.fcd_origin_lot_id:
                line.purchase_price = line.lot_id.fcd_origin_lot_id.fcd_document_line_id.price_real_kg
            elif line.lot_id.fcd_document_line_id:
                line.purchase_price = line.lot_id.fcd_document_line_id.price_real_kg

    @api.constrains('product_uom_qty')
    def _contrains_drag_to_stock_move(self):
        dones = self.move_ids.filtered(lambda x: x.state == 'done')
        if len(dones) == 0:
            move_id = self.move_ids.filtered(lambda x: x.state != 'cancel')
            if len(move_id) == 1 and self.product_uom_qty < move_id.product_uom_qty:
                move_id.product_uom_qty = self.product_uom_qty

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
            'context': {'inventory_mode': True}
        }

    def action_remove_lot(self):
        self.ensure_one()
        self.lot_id = False
        self.lot_location_id = False
