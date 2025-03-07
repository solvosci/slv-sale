# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Partner Data Security",
    "summary": "Restrict partner information changes on the sales order by security group.",
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Sales",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": [
        "sale",
        "partner_readonly_security",
        "sale_invoice_policy",
        "account_payment_sale"
    ],
    "data": [
        "security/security.xml",
        "views/sale_order_views.xml"
    ],
}
