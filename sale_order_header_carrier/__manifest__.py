# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Header Carrier",
    "summary": """
        Makes possible to define a carrier at sale order header level.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "delivery_auto_refresh",
    ],
    "data": [
        "views/sale_order_views.xml",
    ],
    'installable': True,
}
