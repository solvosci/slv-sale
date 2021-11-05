# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    tasks_count = fields.Integer(related="invoice_line_ids.sale_line_ids.order_id.tasks_count")
