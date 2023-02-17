# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Invoice Plan - pending planned invoices",
    "summary": """
        Shows pending planned invoices for the Sale Order
        according to its Invoice Plan
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_invoice_plan", "sale_order_invoice_qty_number"],
    "data": ["views/sale_order_views.xml"],
    'installable': True,
}
