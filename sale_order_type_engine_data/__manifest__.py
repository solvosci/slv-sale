# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Type Engine Data",
    "summary": """
        Adds engine data in the sales order types. 
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_order_engine_data",
        "sale_order_type",
    ],
    "data": [
        "views/sale_order_type_views.xml",
        "views/sale_order_views.xml",
    ],
    'installable': True,
}
