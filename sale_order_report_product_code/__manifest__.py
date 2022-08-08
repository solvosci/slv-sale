# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Report - Add product code",
    "summary": """
        Splits Sale Order Report in two, in order to provide a new one with
        the product code column
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.1",
    "category": "Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale",
        "reports_ar"
    ],
    "data": [
        "report/sale_report_templates.xml",
        "report/sale_report.xml",
    ],
    'installable': True,
}
