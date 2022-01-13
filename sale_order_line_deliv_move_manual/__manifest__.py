# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Line - Manual Move based Delivery Quantity",
    "summary": """
        Sets a new product invoice policy, so it can be based on manually
        done destination quantities in stock moves
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_stock"],
    "data": [
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
    ],
    'installable': True,
}
