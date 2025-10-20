# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Partner Selectable Option Extended",
    "summary": "Extends the Sale Partner Selectable Option module to restrict the selectable option to contacts and if it is not a contact, it will inherit the parent's selectable option.",
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sales Management",
    "website": "https://github.com/solvosci/slv_sale",
    "depends": [
        "sale",
        "sale_partner_selectable_option"
        ],
    "data": [
        "views/res_partner_view.xml",
        ],
}
