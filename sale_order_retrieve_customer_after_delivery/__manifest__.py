# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Retrieve Customer After Delivery",
    "summary": """
        Put delivery addres before customer and retrieve the customer after delivery address.
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
        "views/sale_order_views.xml",
    ],
    'pre_init_hook': 'pre_init_hook',
    'installable': True,
}
