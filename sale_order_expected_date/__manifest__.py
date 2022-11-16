# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    "name": "Sale Order Expected Date",
    "summary": """
        Calculates the estimated material delivery date from a quote/order
        and shows it in Sales Order report
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "",
    "depends": [
        "sale",
    ],
    "data": [
        "views/sale_order_views.xml",
        'report/sale_report.xml'
    ],
    'installable': True,
}
