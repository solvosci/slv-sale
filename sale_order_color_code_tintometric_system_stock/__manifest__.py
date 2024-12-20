# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Color Code Tintometric System Stock",
    "summary": """
        Add column 'Lot/S.Tin' indicating the color code of the tintometric system.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_order_color_code_tintometric_system",
        "sale_stock"
    ],
    "data": [
        "views/stock_picking_views.xml",
        "reports/stock_picking_template.xml",
        "views/stock_move_views.xml",
        "reports/stock_picking_operations_template.xml"
    ],
    'installable': True,
}
