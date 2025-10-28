# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Field Advanced",
    "summary": """
        Add fields to sale order lines and a new menu to manage them.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.3.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/sale_order_field_advanced_security.xml',
        'wizards/sale_order_line_manufacturing_state_wizard_views.xml',
        'wizards/sale_order_line_complement_tag_state_wizard_views.xml',
        'views/sale_order_line_modification_views.xml',
        'views/sale_order_line_process_status_views.xml',
        'data/sale_order_line_process_status_data.xml',
        'views/sale_order_line_views.xml',
        'views/product_category_views.xml',
        'views/product_template_views.xml',
        'views/sale_order_field_advanced_menu.xml',
        'views/product_complement_size.xml'
    ],
    'installable': True,
}
