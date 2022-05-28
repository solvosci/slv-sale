# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sales Order Project Archive",
    "summary": """
        (Un)archive Sales Order related Projects when order is (un)locked
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_project"],
    "post_init_hook": "post_init_hook",
    "installable": True,
}
