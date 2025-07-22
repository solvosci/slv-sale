# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from . import models
from odoo.tools import sql
import logging

_logger = logging.getLogger(__name__)


def pre_init_hook(env):
    """This hook is used to link a sales order to existing pending moves
    when the sale_order_pending_move_menu module is installed.
    """
    if not sql.column_exists(env.cr, "stock_move", "move_sale_order_id"):
        sql.create_column(env.cr, "stock_move", "move_sale_order_id", "integer")

    _logger.info("Initializing move_sale_order_id field")
    env.cr.execute("""
        UPDATE stock_move m
        SET move_sale_order_id = l.order_id
        FROM sale_order_line l
        WHERE m.sale_line_id = l.id
        AND m.sale_line_id IS NOT NULL;
    """)
