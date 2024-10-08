# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Warehouse Header",
    "summary": """
        Moves warehouse field in sales orders form to header, so it becomes more accessible.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_stock",
    ],
    "data": [
        "views/sale_order_views.xml",
    ],
    'installable': True,
}
