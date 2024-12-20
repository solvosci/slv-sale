# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ColorTintometricSytemMixin(models.AbstractModel):
    _name = "color.tintometric.system.mixin"
    _description = "Color Tintometric System Mixin"

    color_code_tintometric = fields.Char(string="Lot/S.Tin", copy=False)
