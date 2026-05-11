# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Line Set Price Field",
    "summary": """
        New 'set price' field on sale order lines, this field must be filled in if the order is to be confirmed.
        In addition, there is a “set_price_sale_order” field that allows you to modify the value of the 'set price'
        field for all lines in the sale order.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "13.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "views/sale_order_views.xml",
        "views/sale_order_line_views.xml",
    ],
    'installable': True,
}
