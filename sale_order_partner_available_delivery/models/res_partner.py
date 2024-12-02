# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_available = fields.Boolean(compute="_compute_sale_available", store=True)

    @api.depends("type", "parent_id", "child_ids.type")
    def _compute_sale_available(self):
        for record in self:
            if record.type == "delivery":
                record.sale_available = True
            else:
                if record.parent_id:
                    record.sale_available = False
                else:
                    if len(record.child_ids.filtered(lambda x: x.type == "delivery")) > 0:
                        record.sale_available = False
                    else:
                        record.sale_available = True
