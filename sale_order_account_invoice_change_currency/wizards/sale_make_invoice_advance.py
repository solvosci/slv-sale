# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"
    _description = "Sales Advance Payment Invoice"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        invoice_vals = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(order, name, amount, so_line)
        if so_line.order_id.is_custom_rate:
            invoice_vals['original_currency_id'] = self.env.company.currency_id
            invoice_vals['custom_rate'] = so_line.order_id.custom_rate
            for line in invoice_vals['invoice_line_ids']:
                line.original_price_unit /= invoice_vals['custom_rate']

        return invoice_vals
