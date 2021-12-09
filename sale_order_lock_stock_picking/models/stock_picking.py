# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    sale_order_status = fields.Selection(related="sale_id.state")

    def lock_validation_error(self, sale_id):
        """
        When a picking is done, it's not possible changing quants, so we
        enable editing it
        TODO cancel state management
        """
        if self.state != "done" and sale_id.state == "done":
            raise ValidationError( _(
                "The related sales order (%s) is locked. Unlock it to continue."
                ) % sale_id.name
            )

    def button_validate(self):
        self.lock_validation_error(self.sale_id)
        return super(StockPicking, self).button_validate()        

    def action_toggle_is_locked(self):
        self.lock_validation_error(self.sale_id)
        return super(StockPicking, self).button_validate()        

    def write(self, vals):
        for record in self:
            record.lock_validation_error(record.sale_id)
        return super(StockPicking, self).write(vals)

    @api.model
    def create(self, vals):
        # Sale soft link when manually adding a picking
        # sale_id is not filled at this moment
        sale_id = self.env['sale.order'].search([('name', '=', vals.get('origin'))])
        if sale_id and sale_id.state == "done":
            raise ValidationError( _(
                "The related sales order (%s) is locked. Unlock it to continue."
                ) % sale_id.name
            )
        return super(StockPicking, self).create(vals)
