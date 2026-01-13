# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Product Supplierinfo For Customer Sale Sol Code Hide",
    "summary": """
        By default product_customer_code field is hidden
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["product_supplierinfo_for_customer_sale"],
    "data": [
        "views/sale_order_view.xml"
    ],
    'installable': True,
}
