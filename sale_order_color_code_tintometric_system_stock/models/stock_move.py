# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = "stock.move"
    
    color_code_tintometric = fields.Char(related="sale_line_id.color_code_tintometric", string="Lot/S.Tin")
