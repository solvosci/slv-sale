# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Order - Link with Account Invoice Change Currency",
    "summary": """
        Adds support for manual currency rate from sales order to invoice
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale", "account_invoice_change_currency"],
    "data": ["views/sale_order_views.xml"],
    'installable': True,
}
