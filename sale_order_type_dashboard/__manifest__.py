# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Type Dashboard",
    "summary": """
        Adds a dashboard for Sale Orders based on Sale Order Types.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_order_type"],
    "data": [
        "views/menu_sale_order.xml",
        "views/sale_order_views.xml",
        "views/sale_order_type_views.xml",
    ],
    "installable": True,
}
