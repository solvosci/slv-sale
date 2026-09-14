# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Order Financial Risk Zero",
    "summary": """
        By default, if risk limit on sales orders of a customer is exactly zero,
        all sales orders will be blocked, except if the order is exactly zero.
        Now if that condition is true, it also blocks the order.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_financial_risk"],
    'installable': True,
}
