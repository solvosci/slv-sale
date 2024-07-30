# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Engine Data",
    "summary": """
        Adds new fields for engine data
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale",
    ],
    "data": [
        "views/sale_order_views.xml",
        "reports/sale_order_template.xml",
        "reports/account_move_templates.xml",
    ],
    'installable': True,
}
