# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale Order Line Advanced",
    "summary": """
        Adds create mode and some fields to Sale Order Line tree:
            - Date Order
    """,
    "version": "14.0.1.0.0",
    "author": "Solvos",
    "license": "LGPL-3",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "views/sale_order_line_views.xml",
    ],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
