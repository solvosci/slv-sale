# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Lock Stock Picking",
    "summary": """
        Adds restriction when trying to create or edit a 
        stock picking that is linked to a locked sales order 
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale_stock"],
    "data": [
        "views/stock_picking_views.xml",    
    ],
    'installable': True,
}
