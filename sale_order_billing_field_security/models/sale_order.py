# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, api
from lxml import etree


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        result = super().get_view(view_id=view_id, view_type=view_type, **options)
        group = "account.group_account_manager"
        if view_type == "form" and not self.env.user.has_group(group):
            restricted_fields = [
                'pricelist_id',
                'type_id',
                'payment_term_id',
                'invoice_policy',
                'payment_mode_id',
                'partner_invoice_id',
                'partner_shipping_id',
                'user_id',
                'team_id',
                'company_id',
                'fiscal_position_id',
                'journal_id',
                'mandate_id',
            ]
            doc = etree.XML(result["arch"])
            for field in restricted_fields:
                for node in doc.xpath(f"//field[@name='{field}']"):
                    node.set("readonly", "1")
                    node.set("force_save", "1")
            result["arch"] = etree.tostring(doc, encoding="unicode")
        return result
