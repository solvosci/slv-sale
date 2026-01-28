# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, _, fields, api
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    offer_price = fields.Boolean(compute="_compute_offer_price")

    def get_last_purchase_invoice_line(self, product):
        move_line = self.env['account.move.line'].search([
            ('product_id', '=', product),
            ('quantity', '>', 0),
            ('move_id.move_type', '=', 'in_invoice'),
            ('move_id.state', '=', 'posted'),
            ('display_type', '=', 'product'),
        ], limit=1, order='date desc')
        return {
            "move_line": move_line,
            "move_line_id": move_line.id
        }

    def _compute_amount(self):
        super()._compute_amount()
        if not self.env.user.has_group('sale_order_net_price_control.group_sale_at_any_price'):

            for record in self.filtered(lambda r: r.product_id and r.product_uom_qty > 0):

                net_price_sale = record.price_subtotal / record.product_uom_qty

                purchase_invoice = self.get_last_purchase_invoice_line(record.product_id.id)["move_line"]
                # self.env['account.move.line'].search([
                #     ('product_id', '=', record.product_id.id),
                #     ('quantity', '>', 0),
                #     ('move_id.move_type', '=', 'in_invoice'),
                #     ('move_id.state', '=', 'posted'),
                #     ('display_type', '=', 'product'),
                # ], limit=1, order='date desc')

                if purchase_invoice:
                    invoice_line = purchase_invoice.filtered(
                    lambda x: x.product_id.id == record.product_id.id
                    )
                    net_price_purchase = invoice_line.price_subtotal / invoice_line.quantity

                    if net_price_sale <= net_price_purchase:
                        raise ValidationError(_(
                            "Net price of '%s', '%.2f' must be higher that the last purchase invoice price '%s'"
                        )%(record.product_template_id.name,net_price_sale,net_price_purchase) )

                if self.get_control_pricelist() != False:
                    pricelist = record.get_price_from_lowest_pricelist_id(
                        product_template_id=record.product_template_id.id,
                        quantity=record.product_uom_qty,
                        pricelist_id=self.get_control_pricelist(),
                    )
                    rules = (
                        not record.offer_price
                        and pricelist[0] != 999999
                        and not (net_price_sale == pricelist[0] == 0)
                    )
                    if rules and net_price_sale <= pricelist[0]:
                        raise ValidationError(_(
                            "Net price of '%s', '%.2f' must be higher that the lowest pricelist '%s', '%s'"
                        )%(record.product_template_id.name,net_price_sale,self.env.user.company_id.lowest_pricelist_id.name,pricelist[0]))

    # def get_price_from_lowest_pricelist_id(self):
        # _logger.warning("UOM del producto: %s", self.product_uom.id)
        # _logger.warning("UOM base del producto: %s", self.product_id.uom_id.id)
        # _logger.warning("UOM POS: %s", self.env.context.get("uom"))
        # pricelist_id = self.get_control_pricelist()
        # ctx = {
        #     "pricelist": pricelist_id,
        #     "partner_id": self.order_id.partner_id.id,
        #     "quantity": self.product_uom_qty,
        #     "uom": self.product_uom.id,
        #     "company_id": self.order_id.company_id.id,
        # }
        # sale_order_obj = self.env['sale.order'].with_context(ctx)

        # order_line_vals = [{
        #     "product_id": self.product_id.id,
        #     "product_uom_qty": self.product_uom_qty,
        #     "order_id": False,
        # }]

        # so_vals = {
        #     "partner_id": self.order_id.partner_id.id,
        #     "pricelist_id": pricelist_id,
        #     "order_line": order_line_vals,
        # }
        # valued_order = sale_order_obj.new(so_vals)

        # price = valued_order.order_line.price_unit
        # discount = valued_order.order_line.discount
        # return price - (price * (discount/100))

    @api.model
    def get_price_from_lowest_pricelist_id(self, **kwargs):
        product_tmpl_id = kwargs.get("product_template_id")
        product_id = kwargs.get("product_id")
        quantity = kwargs["quantity"]
        pricelist_id = kwargs["pricelist_id"]

        if product_id:
            product = self.env['product.product'].browse(product_id)
        if product_tmpl_id:
            product = self.env['product.template'].browse(product_tmpl_id).product_variant_id
        pricelist = self.env['product.pricelist'].browse(pricelist_id)

        price = pricelist._get_product_price_rule(
            product,
            quantity,
            uom=product.uom_id,
            date=fields.Date.context_today(self),
        )

        return price

    @api.depends('product_id')
    def _compute_offer_price(self):
        for line in self:
            line.offer_price = False
            for item in line.company_id.lowest_pricelist_id.item_ids.filtered(lambda x:x.product_tmpl_id == line.product_template_id):
                line.offer_price = item.offer_price

    def get_control_pricelist(self):
        company = self._context.get("company_id", False) and self.env["res.company"].browse(
            self._context["company_id"]
        ) or self.env.user.company_id
        return company.lowest_pricelist_id.id
