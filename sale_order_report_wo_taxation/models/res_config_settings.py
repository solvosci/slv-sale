# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_taxes_on_report_saleorder_document = fields.Boolean(string="Taxes", implied_group="sale_order_report_wo_taxation.group_taxes_on_report_saleorder_document")
