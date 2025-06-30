# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from openupgradelib import openupgrade


def post_init_hook(env):
    openupgrade.load_data(
        env, "sale_stock_security", "data/noupdate_changes.xml"
    )

def uninstall_hook(env):
    (env.ref("sale.sale_order_see_all") |
    env.ref("sale.sale_order_line_see_all")).write({"domain_force": str([(1,'=',1)])})
