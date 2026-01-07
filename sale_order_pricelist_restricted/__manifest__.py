# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order - Restrict Pricelist selection",
    "summary": """
        Enables some restrictions about pricelist selection within a Sales Order
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "security/sale_order_pricelist_restricted.xml",
        "views/product_pricelist_views.xml",
        "views/sale_order_views.xml",
    ],
}
