# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api, _
from odoo.exceptions import ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def lock_validation_error(self, sale_id):
        if sale_id.state == 'done':
            raise ValidationError( _(
                "The related sales order (%s) is locked. Unlock it to continue."
                ) % sale_id.name
            )

    def write(self, values):
        for record in self.filtered(lambda x: x.project_id.sale_order_id):
            self.lock_validation_error(record.project_id.sale_order_id)
        return super(AccountAnalyticLine, self).write(values)

    @api.model_create_multi
    def create(self, vals_list):
        Project = self.env['project.project']
        for vals in vals_list:
            project_id = (
                vals.get('project_id', False)
                and Project.browse(vals.get('project_id'))
            )
            if project_id and project_id.sale_order_id:
                self.lock_validation_error(project_id.sale_order_id)
        return super(AccountAnalyticLine, self).create(vals_list)

    def unlink(self):
        for record in self.filtered(lambda x: x.project_id.sale_order_id):
            self.lock_validation_error(record.project_id.sale_order_id)
        return super().unlink()
