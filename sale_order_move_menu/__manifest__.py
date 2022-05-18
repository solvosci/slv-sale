# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Move Menu",
    "summary": """
        Adds new menu for sale related moves
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.2.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_stock"],
    "data": [
        "views/stock_move_views.xml",
        "views/sale_order_views.xml",
    ],
    'installable': True,
}
