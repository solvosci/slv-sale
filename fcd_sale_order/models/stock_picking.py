# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _action_done(self):
        res = super(StockPicking, self)._action_done()
        for picking in self.filtered(lambda x: x.sale_id):
            for record in picking.move_line_ids_without_package.filtered(lambda x: x.move_id.sale_line_id and x.lot_id):
                record.lot_id.check_and_log_stock_balance("T1.C Action Done Sale Picking", picking.name)
        return res
