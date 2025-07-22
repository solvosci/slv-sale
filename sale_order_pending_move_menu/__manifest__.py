# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Pending Move Menu",
    "summary": """
        New menu that show sale line information from stock moves
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_stock"],
    "data": [
        "views/stock_move_views.xml",
        "views/sale_order_pending_move_menu.xml",
    ],
    "pre_init_hook": "pre_init_hook",
    'installable': True,
}
