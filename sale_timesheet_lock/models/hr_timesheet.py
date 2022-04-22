# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models, api, _
from odoo.exceptions import ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _get_locked_fields(self):
        """
        Override if needed
        """
        return ["project_id", "task_id", "unit_amount"]

    def lock_validation_error(self, sale_id):
        if sale_id.state == 'done':
            raise ValidationError( _(
                "The related sales order (%s) is locked. Unlock it to continue."
                ) % sale_id.name
            )

    def write(self, values):
        """
        Editing a timesheet for non-sensible fields is enabled
        """
        val_fields = values.keys()
        lock_fields = self._get_locked_fields()
        if any([field in val_fields for field in lock_fields]):
            self_sudo = self.sudo()
            for record in self_sudo.filtered(lambda x: x.project_id.sale_order_id):
                self.lock_validation_error(record.project_id.sale_order_id)
        return super(AccountAnalyticLine, self).write(values)

    @api.model_create_multi
    def create(self, vals_list):
        ProjectSudo = self.env['project.project'].sudo()
        for vals in vals_list:
            project_id = (
                vals.get('project_id', False)
                and ProjectSudo.browse(vals.get('project_id'))
            )
            if project_id and project_id.sale_order_id:
                self.lock_validation_error(project_id.sale_order_id)
        return super(AccountAnalyticLine, self).create(vals_list)

    def unlink(self):
        self_sudo = self.sudo()
        for record in self_sudo.filtered(lambda x: x.project_id.sale_order_id):
            self.lock_validation_error(record.project_id.sale_order_id)
        return super().unlink()
