# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Partner Invoice Period",
    "summary": """ Adds selection of period to invoice direction """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.3.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale"
    ],
    "data": [
        "views/res_partner_view.xml",
        "views/sale_order_view.xml",
        "views/res_config_settings.xml"
    ],
    'installable': True,
}
