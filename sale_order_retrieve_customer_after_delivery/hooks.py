from odoo.tools import column_exists, create_column

def pre_init_hook(env):
   
    if not column_exists(env.cr, "sale_order", "partner_shipping_2_id"):
        create_column(env.cr, "sale_order", "partner_shipping_2_id", "integer")

    query = """
        UPDATE sale_order
        SET partner_shipping_2_id = partner_shipping_id
        WHERE partner_shipping_id IS NOT NULL;
    """
    env.cr.execute(query)
