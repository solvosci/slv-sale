# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Client Order Ref Autofill",
    "summary": """
        Adds autofills Customer Reference field when an order is confirmed.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_order_client_order_ref_mandatory",
        "sale_order_type",
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/sale_order_type_views.xml",
        "data/ir_sequence.xml",  
    ],
    'installable': True,
}
