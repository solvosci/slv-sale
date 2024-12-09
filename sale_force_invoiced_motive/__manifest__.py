# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Force Invoiced Motive",
    "summary": "Adds a motive to a forced invoice",
    "version": "17.0.1.0.0",
    "author": "Solvos",
    "category": "sale",
    "license": "LGPL-3",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale",
                "sale_force_invoiced"],
    "data": [
        "security/security.xml",
        "views/sale_order_view.xml",
        "wizard/force_invoiced_motive_wizard_view.xml",
    ],
    "installable": True,
}
