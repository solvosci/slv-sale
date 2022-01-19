# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    product_categ_id = fields.Many2one(related='product_id.categ_id')
    currency_id = fields.Many2one(related='sale_line_id.currency_id')
    sale_order = fields.Many2one(related='sale_line_id.order_id', store=True)
    sale_partner_id = fields.Many2one(related='sale_order.partner_id', store=True)
    sale_price_unit = fields.Float(related='sale_line_id.price_unit')
    sale_price_amount_total = fields.Monetary(
        compute="_compute_sale_price_amount_total",
        string="Amount Total",
        store=True,
    )

    @api.depends("sale_price_unit", "quantity_done")
    def _compute_sale_price_amount_total(self):
        for record in self:
            record.sale_price_amount_total = record.sale_price_unit * record.quantity_done
