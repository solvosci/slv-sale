# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Partner Available Delivery",
    "summary": """
        Only customers and delivery addresses can be selected as customers in sale orders.
        Now, the delivery address cannot be edited.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale",
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
    ],
    'installable': True,
}
