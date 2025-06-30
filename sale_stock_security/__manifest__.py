# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Stock Security",
    "summary": """
        Now users belonging to the group ‘User: All documents’ will only see orders from their warehouse.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_stock"],
    "data": [
        "security/sale_stock_security.xml",
        "data/noupdate_changes.xml",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    'installable': True,
}
