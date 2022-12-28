# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    fcd_import = fields.Boolean(string="Import")

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        if not self.partner_shipping_id.parent_id:
            super().onchange_partner_id()

    @api.onchange("partner_shipping_id")
    def _onchange_shipping_id(self):
        if self.partner_shipping_id.parent_id:
            self.partner_id = self.partner_shipping_id.parent_id
            self.partner_invoice_id = self.partner_shipping_id.parent_id
        else:
            self.partner_id = self.partner_shipping_id
            self.partner_invoice_id = self.partner_shipping_id
        self.pricelist_id = self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False

    @api.constrains('fcd_import')
    def _constrains_fcd_import(self):
        if self.fcd_import:
            for line in self.order_line:
                #TODO: Check conversion to avoid reference assignment
                import_qty = float(line.product_uom_qty)
                line.secondary_uom_id = line.product_id.sale_secondary_uom_id.id
                line.product_uom_qty = import_qty
                line.lot_id = line.lot_id.search([('name', '=', line.lot_id.name), ('product_id', '=', line.product_id.id)])

    def action_sale_order_confirm_multi(self):
        super(SaleOrder, self).action_sale_order_confirm_multi()
        for picking_id in self.browse(self.env.context['active_ids']).filtered(lambda x: x.state == 'sale').picking_ids.filtered(lambda x: x.state in ('draft', 'waiting', 'confirmed', 'assigned')):
            for move_id in picking_id.move_ids_without_package:
                move_id.action_complete_stock_move_line()
            picking_id.action_confirm()
            picking_id.action_assign()
            picking_id._action_done()
