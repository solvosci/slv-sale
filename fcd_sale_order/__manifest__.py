# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "FCD Sale Order",
    "summary": """
        Adds sale order link with fcd
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.1.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "fcd_weight_scale_mrp",
        "sale_order_lot_selection",
        "sale_margin",
        "sale_order_secondary_unit",
        "sale_order_action_confirm_multi",
        "stock_secondary_unit_stock_quant",
    ],
    "data": [
        "report/sale_report_templates.xml",
        "security/fcd_sale_order_security.xml",
        "security/ir.model.access.csv",
        "views/sale_order_line_views.xml",
        "views/sale_order_views.xml",
        "views/stock_move_views.xml",
        "views/stock_move_line_views.xml",
        "wizards/fcd_stock_quant_wizard_views.xml",
    ],
    'installable': True,
}
