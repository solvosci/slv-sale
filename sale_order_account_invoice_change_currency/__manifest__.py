# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)
{
    "name": "Sale Order Account Invoice - Change Currency",
    "summary": """
        Allows you to modify the rate when the invoice is issued with a currency other than the main one.
    """,
    "version": "13.0.1.10.0",
    "category": "Accounting & Finance",
    "website": "https://github.com/solvosci/slv-account",
    "author": "Solvos",
    "license": "LGPL-3",
    "depends": ["sale","account_invoice_change_currency"],
    "data": ["views/sale_order_views.xml"],
    "installable": True,
}
