# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Secondary Unit",
    "summary": "Sale product in a secondary unit",
    "version": "14.0.1.0.0",
    "category": "Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "author": "Solvos",
    "license": "LGPL-3",
    "auto_install": True,
    "depends": [
        "sale",
        "product_secondary_unit"
    ],
    "data": [
        "views/product_views.xml",
        "views/sale_order_views.xml"
    ],
    "installable": True,
}
