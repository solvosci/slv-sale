# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("type_id")
    def _onchange_terms_type_id(self):
        if self.type_id.terms_template_id:
            self.terms_template_id = self.type_id.terms_template_id
            self._onchange_terms_template_id()
