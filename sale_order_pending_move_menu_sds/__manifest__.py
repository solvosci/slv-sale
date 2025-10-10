# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Order Pending Move Menu Link Sale Delivery State",
    "summary": """
        Link ‘sale_order_pending_move_menu’ and sale_delivery_state to add the 'delivery_status' field to the 'pending sales moves' view
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_delivery_state", "sale_order_pending_move_menu"],
    "data": [
        "views/stock_move_views.xml",
    ],
    'installable': True,
}
