# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Sale Partner Security",
    "summary": """
        Limit which contacts an Odoo user can see based on the sales representative
        assigned to that contact and the different permissions in Sales for the Odoo user.
        - User: Own Documents Only: they can see the contacts they are salespeople for, followers,
        or the contact they themselves are and view all contacts associated with Odoo users.
        - User: All Documents: see all contacts
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    'category': "Operations/Sale",
    "website": "https://github.com/solvosci/slv-sale",
    "depends": ["sale"],
    "data": [
        "security/sale_partner_security.xml"
    ],
    'installable': True,
}
