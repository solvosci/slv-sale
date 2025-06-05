# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, _, fields
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    offer_price = fields.Boolean(related='pricelist_item_id.offer_price', store=True)

    def _compute_amount(self):
        super()._compute_amount()
        if not self.env.user.has_group('sale_order_net_price_control.group_sale_at_any_price'):

            for record in self.filtered(lambda r: r.product_id and r.product_uom_qty > 0):

                net_price_sale = record.price_subtotal / record.product_uom_qty

                purchase_invoice = self.env['account.move.line'].search([
                    ('product_id', '=', record.product_id.id),
                    ('quantity', '>', 0),
                    ('move_id.move_type', '=', 'in_invoice'),
                    ('move_id.state', '=', 'posted'),
                    ('display_type', '=', 'product'),
                ], limit=1, order='date desc')

                if purchase_invoice:
                    invoice_line = purchase_invoice.filtered(
                    lambda x: x.product_id.id == record.product_id.id
                    )
                    net_price_purchase = invoice_line.price_subtotal / invoice_line.quantity

                    if net_price_sale <= net_price_purchase:
                        raise ValidationError(_(
                            "Net price of '%s', '%.2f' must be higher that the last purchase invoice price '%s'"
                        )%(record.product_template_id.name,net_price_sale,net_price_purchase) )

                if not record.offer_price and record._get_price_from_lowest_pricelist_id() != 999999 and not (net_price_sale == record._get_price_from_lowest_pricelist_id() == 0):
                    if net_price_sale <= record._get_price_from_lowest_pricelist_id():
                        raise ValidationError(_(
                            "Net price of '%s', '%.2f' must be higher that the lowest pricelist '%s', '%s'"
                        )%(record.product_template_id.name,net_price_sale,self.env.user.company_id.lowest_pricelist_id.name,record._get_price_from_lowest_pricelist_id()))

    def _get_price_from_lowest_pricelist_id(self):
        company = self._context.get("company_id", False) and self.env["res.company"].browse(
            self._context["company_id"]
        ) or self.env.user.company_id

        sale_order_obj = self.env['sale.order']

        order_line_vals = []
        for line in self:
            line_vals = {
                "product_id": line.product_id.id,
                "product_uom_qty": line.product_uom_qty,
                "order_id": False,
            }
            order_line_vals.append(line_vals)

        so_vals = {
            "partner_id": self.order_id.partner_id.id,
            "pricelist_id": company.lowest_pricelist_id.id,
            "order_line": order_line_vals,
        }
        valued_order = sale_order_obj.new(so_vals)

        price = valued_order.order_line.price_unit
        discount = valued_order.order_line.discount
        return price - (price * (discount/100))
