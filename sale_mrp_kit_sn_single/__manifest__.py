# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    "name": "Sale MRP - ensure single moves for S/N products",
    "summary": """
        For S/N tracked products, ensures that pickings moves created from a
        sale kit product are created with 1.0 quantity each one
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Sales/Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_mrp"],
    "installable": True,
}
