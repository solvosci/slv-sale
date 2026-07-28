# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import logging


def pre_init_hook(cr):
    logging.getLogger('odoo.addons.sale_order_line_advanced').info(
        'Updating sale.order.line with date orders field to True')

    logging.getLogger("Add sale_order_line date_order column if it does not yet exist")
    cr.execute(
        """
        ALTER TABLE "sale_order_line"
        ADD COLUMN IF NOT EXISTS "date_order" TIMESTAMP WITHOUT TIME ZONE
        """
    )
    cr.execute(
        """
        ALTER TABLE "sale_order_line"
        ADD COLUMN IF NOT EXISTS "last_update_order" TIMESTAMP WITHOUT TIME ZONE
        """
    )
    cr.execute(
        """
        UPDATE sale_order_line
        SET 
            date_order = sale_order.date_order,
            last_update_order = sale_order.write_date
        FROM sale_order
        WHERE sale_order_line.order_id = sale_order.id
        """
    )
