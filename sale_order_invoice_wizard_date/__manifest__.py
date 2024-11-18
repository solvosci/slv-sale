# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Invoice Wizard Date",
    "summary": """
        Add “invoice date” field when creating multiple order invoices to be included in draft invoices
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [        
        "wizard/sale_make_invoice_advance_views.xml",
    ],
    'installable': True,
}
