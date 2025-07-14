# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Picking No Create",
    "summary": """
        Disables the creation of stock pickings and move from the Sales Order "Pickings" button.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_stock",
        "stock_picking_no_create_base",
    ],
    'installable': True,
}
