# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import  models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    expected_days = fields.Float(compute='_compute_expected_days')
    expected_date = fields.Datetime()
 

    def _compute_expected_date(self):
        """ For service and consumable, we only take the min dates. This method is extended in sale_stock to
            take the picking_policy of SO into account.
        """
        super()._compute_expected_date()
        self.mapped("order_line")  
        for order in self:
            dates_list = []
            for line in order.order_line.filtered(lambda x: x.state != 'cancel' and not x._is_delivery() and not x.display_type):
                dt = line._expected_date()

                dates_list.append(dt)
            if dates_list:
                order.expected_date = fields.Datetime.to_string(max(dates_list))
            else:
                order.expected_date = False

        
    def _compute_expected_days(self):
        for record in self:
            if record.state in ["sale", "done", "cancel"]:
                record.expected_days = 0
            elif record.commitment_date:
                record.expected_days = (record.commitment_date - fields.Datetime.now()).days
            else:
                leads = record.order_line.filtered(
                    lambda x: x.state != 'cancel' and not x._is_delivery() and not x.display_type
                ).mapped("customer_lead")
                if leads:
                    record.expected_days = max(leads)
                else:
                    record.expected_days = 0
