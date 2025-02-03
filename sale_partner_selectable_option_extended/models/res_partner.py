# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    sale_selectable = fields.Boolean(
        compute="_compute_sale_selectable",
        store=True,
        readonly=False,
        recursive=True,
        )

    @api.depends("type", "parent_id", "parent_id.sale_selectable")
    def _compute_sale_selectable(self):
        for partner in self:
            if partner.type != "contact" and partner.parent_id:
                partner.sale_selectable = partner.parent_id.sale_selectable
