# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Line Project Task",
    "summary": """
        Adds editable task_id field in sale order lines that your product is storable
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.1",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_project",
        "sale_stock"
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "views/stock_move_views.xml",
        "views/account_move_views.xml",
        "views/stock_move_line_views.xml",
    ],
    'installable': True,
}
