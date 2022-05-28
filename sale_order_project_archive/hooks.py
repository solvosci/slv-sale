# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import logging

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    logger = logging.getLogger("odoo.addons.sale_order_project_archive")
    logger.info("Archiving existing projects in done/cancel sales orders")

    env = api.Environment(cr, SUPERUSER_ID, {})
    sale_orders = env["sale.order"].search(
        [("state", "in", ["done", "cancel"])]
    )
    projects = sale_orders.mapped("order_line.project_id")
    projects_no = len(projects)
    if projects:
        projects.write({"active": False})
    logger.info("Archived projects: %d" % projects_no)
