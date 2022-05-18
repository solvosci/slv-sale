# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Order Move Menu - Link to Invoices",
    "summary": """
        Adds invoice data (such as invoice date) to sale related moves menu
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.2.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_order_move_menu",
        "stock_picking_invoice_link",
        "web_tree_dynamic_colored_field"
    ],
    "data": [
        "views/stock_move_views.xml",
    ],
    'installable': True,
}
