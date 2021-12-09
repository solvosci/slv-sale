# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import _, models
from odoo.exceptions import ValidationError


class StockReturnPicking(models.TransientModel):
    _inherit = "stock.return.picking"

    def create_returns(self):
        for wizard in self:
            if wizard.picking_id.sale_order_status == "done":
                raise ValidationError( _(
                    "The related sales order for %s (%s) is locked."
                    " Unlock it to continue."
                    ) % (
                        wizard.picking_id.name, wizard.picking_id.sale_id.name
                    )
                )
            
        return super().create_returns()
