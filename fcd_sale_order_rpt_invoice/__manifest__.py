# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "FCD Sale Order Report Invoice",
    "summary": """

    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "fcd_sale_order",
        "stock_picking_invoice_link"
    ],
    "data": [
        "report/fcd_sale_report_invoice_menuitem.xml",
        "report/fcd_sale_report_invoice_views.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
}
