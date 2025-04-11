# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class SaleOrderLineModification(models.Model):
    _name = 'sale.order.line.modification'
    _description = 'Sale Order Line Modification'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    price = fields.Monetary(currency_field='currency_id')
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company,
        required=True
    )
    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        check_company=True,
    )

    def name_get(self):
        result = []
        for record in self:
            if self._context.get('modification_display_name', False):
                name = f"{record.name}"
            else:
                name = f"{record.name} - {record.price} {record.currency_id.symbol}"
            result.append((record.id, name))
        return result
