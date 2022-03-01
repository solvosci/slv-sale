# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_default_code_hidden = fields.Boolean(
        string='Hidden Internal Reference',
        related='company_id.product_default_code_hidden',
        readonly=False,
    )
    product_inline_description_sale = fields.Boolean(
        string='Description Sale Inline',
        related='company_id.product_inline_description_sale',
        readonly=False,
    )

class ResCompany(models.Model):
    _inherit = 'res.company'

    product_default_code_hidden = fields.Boolean(
        string='Hidden Internal Reference',
    )
    product_inline_description_sale = fields.Boolean(
        string='Description Sale Inline',
    )
