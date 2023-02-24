# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order - (Un)lock extra group",
    "summary": """
        Adds an extra group that enables to (un)lock sale orders
        without being Sales Administrator
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.2.0.0",
    "category": "Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "security/sale_order_unlock_group.xml",
        "views/res_config_settings_views.xml",
        "views/sale_order_views.xml",
    ],
    'installable': True,
}
