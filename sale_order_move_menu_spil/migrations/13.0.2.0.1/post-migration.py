# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 (https://www.gnu.org/licenses/agpl-3.0.html)

from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        sale_move_ids = env['stock.move'].search([
            ('sale_line_id', '!=', False),
            ('state', '=', 'done')
        ])
        sale_move_ids._compute_sale_move_menu()
