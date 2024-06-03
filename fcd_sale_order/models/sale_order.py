# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    fcd_import = fields.Boolean(string="Import")

    # Overwite method https://github.com/odoo/odoo/blob/7f62a1bc7f9410c3d853391d7fdf436536f0c165/addons/sale/models/sale.py#L390
    # Without:
    #   'partner_shipping_id': False,
    #   'partner_shipping_id': addr['delivery'],
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - Pricelist
        - Payment terms
        - Invoice address
        - Delivery address
        - Sales Team
        """
        if not self.partner_id:
            self.update({
                'partner_invoice_id': False,
                'fiscal_position_id': False,
            })
            return

        self = self.with_company(self.company_id)

        addr = self.partner_id.address_get(['delivery', 'invoice'])
        partner_user = self.partner_id.user_id or self.partner_id.commercial_partner_id.user_id
        values = {
            'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
            'payment_term_id': self.partner_id.property_payment_term_id and self.partner_id.property_payment_term_id.id or False,
            'partner_invoice_id': addr['invoice'],
        }
        user_id = partner_user.id
        if not self.env.context.get('not_self_saleperson'):
            user_id = user_id or self.env.uid
        if user_id and self.user_id.id != user_id:
            values['user_id'] = user_id

        if self.env['ir.config_parameter'].sudo().get_param('account.use_invoice_terms') and self.env.company.invoice_terms:
            values['note'] = self.with_context(lang=self.partner_id.lang).env.company.invoice_terms
        if not self.env.context.get('not_self_saleperson') or not self.team_id:
            values['team_id'] = self.env['crm.team'].with_context(
                default_team_id=self.partner_id.team_id.id
            )._get_default_team_id(domain=['|', ('company_id', '=', self.company_id.id), ('company_id', '=', False)], user_id=user_id)
        self.update(values)

    @api.onchange("partner_shipping_id")
    def _onchange_shipping_id(self):
        if self.partner_shipping_id.parent_id:
            self.partner_id = self.partner_shipping_id.parent_id
        else:
            self.partner_id = self.partner_shipping_id

    @api.constrains('fcd_import')
    def _constrains_fcd_import(self):
        if self.fcd_import:
            for line in self.order_line:
                #TODO: Check conversion to avoid reference assignment
                import_qty = float(line.product_uom_qty)
                line.secondary_uom_id = line.product_id.sale_secondary_uom_id.id
                line.product_uom_qty = import_qty
                line.lot_id = line.lot_id.search([('name', '=', line.lot_id.name), ('product_id', '=', line.product_id.id)])

    def action_confirm_order_and_validate_picking(self):
        for order_id in self.browse(self.env.context['active_ids']).filtered(lambda x: x.state in ('draft', 'sent')):
            order_id.action_confirm()
            
            for picking_id in order_id.picking_ids.filtered(lambda x: x.state in ('draft', 'waiting', 'confirmed', 'assigned')):
                for move_id in picking_id.move_ids_without_package:
                    move_id.action_complete_stock_move_line()
                picking_id.action_confirm()
                picking_id.action_assign()
                picking_id._action_done()
