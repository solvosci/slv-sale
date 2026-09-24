# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Net Price Control",
    "summary": """
        Controls the net price of the products when they are sold.
        It has to be higher than the last price on a purchase invoice and higher than the lowest pricelist.
        Allows users who are in the 'Sell Products at Any Price' group to bypass all controls.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "security/sale_order_security.xml",
        "views/res_config_settings_views.xml",
        "views/sale_order_views.xml",
        "views/product_pricelist_item_views.xml"
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "sale_order_net_price_control/static/src/payment.js",
        ],
    },
    'installable': True,
}
