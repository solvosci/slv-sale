# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Color Code Tintometric System",
    "summary": """
        Adds to sale lines column 'Lot/S.Tin' indicating the color code of the tintometric system
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
        "reports/sale_order_template.xml",
        "reports/account_move_template.xml"
    ],
    'installable': True,
}
