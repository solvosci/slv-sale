# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Pending Move Menu Link Website Sale Product Seach Advanced",
    "summary": """
        Link ‘sale_order_pending_move_menu’ and 'website_sale_product_search_advanced'
        to add the 'website_partner_ref' field to the 'pending sales moves' view
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["website_sale_product_search_advanced", "sale_order_pending_move_menu"],
    "data": [
        "views/stock_move_views.xml",
    ],
    'installable': True,
}
