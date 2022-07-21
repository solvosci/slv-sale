# © 2022 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Order Type - Default Terms and conditions Template",
    "summary": """
        For the selected order types, by default a Terms and conditions
        Template can be selected
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.1.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale_order_type",
        "sale_order_note_template",
    ],
    "data": [
        "views/sale_order_type_views.xml",
    ],
    "installable": True,
}
