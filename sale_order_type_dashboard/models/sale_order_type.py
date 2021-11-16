# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrderType(models.Model):
    _inherit = "sale.order.type"

    sale_order_ids = fields.One2many(
        comodel_name="sale.order",
        inverse_name="type_id",
        string="Sale Orders",
    )
    state_quotation_so_count = fields.Integer(
        string="Quotations", compute="_compute_so_counts"
    )
    invoice_status_no_so_count = fields.Integer(
        string="Nothing to Bill", compute="_compute_so_counts"
    )
    invoice_status_ti_so_count = fields.Integer(
        string="Waiting Bills", compute="_compute_so_counts"
    )
    invoice_status_u_so_count = fields.Integer(
        string="Upselling Opportunity", compute="_compute_so_counts"
    )

    @api.depends(
        "sale_order_ids",
        "sale_order_ids.state",
        "sale_order_ids.invoice_status",
    )
    def _compute_so_counts(self):
        quotation_states = ("draft", "sent")
        so_states = ("sale", "done")
        SaleOrder = self.env["sale.order"]
        fetch_data = SaleOrder.read_group(
            [("type_id", "in", self.ids)],
            ["type_id", "state", "invoice_status"],
            ["type_id", "state", "invoice_status"],
            lazy=False,
        )
        result = [
            [
                data["type_id"][0],
                data["state"],
                data["invoice_status"],
                data["__count"],
            ]
            for data in fetch_data
        ]
        for order in self:
            order.state_quotation_so_count = sum(
                [r[3] for r in result if r[0] == order.id and r[1] in quotation_states]
            )
            order.invoice_status_no_so_count = sum(
                [
                    r[3]
                    for r in result
                    if r[0] == order.id and r[1] in so_states and r[2] == "no"
                ]
            )
            order.invoice_status_ti_so_count = sum(
                [r[3] for r in result if r[0] == order.id and r[2] == "to invoice"]
            )
            order.invoice_status_u_so_count = sum(
                [r[3] for r in result if r[0] == order.id and r[2] == "upselling"]
            )
