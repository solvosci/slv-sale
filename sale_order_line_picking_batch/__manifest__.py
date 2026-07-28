# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale Order Line Picking Batch",
    "summary": """
        Adds some fields to Sale Order Line:
            - Stock Picking Batch
    """,
    "version": "14.0.1.0.0",
    "author": "Solvos",
    "license": "LGPL-3",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_stock",
        "stock_picking_batch",
    ],
    "data": [
        "views/sale_order_line_views.xml",
    ],
    "installable": True,
}
