# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    qty_delivered_dest = fields.Float(
        "Destination Delivered Quantity",
        digits="Product Unit of Measure",
        copy=False,
        readonly=True,
        states={"done": [("readonly", False)]},
        help="""
        This field shows the delivered quantity accepted by destination.
        Depending on invoice policy, this field could be used for invoicing
        purposes
        """,
        default=0.0,
    )
    product_invoice_policy = fields.Selection(
        related="product_id.invoice_policy",
    )
