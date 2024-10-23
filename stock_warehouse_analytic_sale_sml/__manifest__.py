# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Stock Warehouse Analytic Sale - Stockl Move Line",
    "summary": """
        Adds analytic tags to sale lines depending on warehouse move lines, 
        this new definition has a higher priority than "Analytic Defaults Rules"
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "category": "Inventory/Purchase",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["stock_warehouse_analytic", "sale_stock"],
    'installable': True,
}
