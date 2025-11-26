# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Order Billing Field Security",
    "summary": """
        Restrict editing of key Sales Order fields to Billing Administration users:
            - pricelist_id
            - payment_term_id
            - partner_invoice_id
            - partner_shipping_id
            - user_id
            - team_id
            - company_id
            - fiscal_position_id
            - journal_id
            - mandate_id (from account_banking_mandate_sale)
            - payment_mode_id (from account_payment_sale)
            - invoice_policy (from sale_invoice_policy)
            - type_id (from sale_order_type)
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "installable": True,
}
