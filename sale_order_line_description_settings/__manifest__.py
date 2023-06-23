# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Line Description Settings",
    "summary": """
        Add some options for the product description like:
            - Hide internal reference
            - Remove line break when you have description sale
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "16.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    'installable': True,
}
