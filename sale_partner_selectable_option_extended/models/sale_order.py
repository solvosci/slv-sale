# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from lxml import etree
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        res = super().get_view(view_id, view_type, **options)
        if view_type == "form":
            order_xml = etree.XML(res["arch"])
            for field_name in ["partner_invoice_id", "partner_shipping_id"]:
                field = order_xml.xpath(f"//field[@name='{field_name}']")
                if field:
                    domain = field[0].get("domain", "[]").replace(
                        "[", "[('sale_selectable', '=', True),")
                    field[0].attrib["domain"] = domain
            res["arch"] = etree.tostring(order_xml)
        return res
