# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Line - Manual Move based Delivery Quantity - Link to stock_picking_invoice_link",
    "summary": """
        Takes in account delivery quantity introduced by
        sale_order_line_deliv_move_manual when link from stock moves to
        invoice lines is generated
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_order_line_deliv_move_manual",
        "stock_picking_invoice_link",
    ],
    'installable': True,
}
