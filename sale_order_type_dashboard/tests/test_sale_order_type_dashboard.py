# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo.tests import common, tagged


@tagged("post_install", "-at_install")
class TestSurchaseOrderTypeDashboard(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.so_obj = cls.env["sale.order"]
        # Partner
        cls.partner1 = cls.env.ref("base.res_partner_1")
        # Products
        cls.product1 = cls.env.ref("product.product_product_7")
        cls.product2 = cls.env.ref("product.product_product_9")
        cls.product3 = cls.env.ref("product.product_product_11")
        # Sale Type
        cls.type1 = cls.env.ref("sale_order_type.normal_sale_type")

    def test_sale_order_type_dashboard(self):
        so_type1_rfq_count = self.type1.state_quotation_so_count
        sale = self._create_sale(
            [(self.product1, 1), (self.product2, 5), (self.product3, 8)]
        )
        self.assertEqual(self.type1.state_quotation_so_count, so_type1_rfq_count + 1)

        sale.action_confirm()
        so_type1_is_no_count = self.type1.invoice_status_no_so_count
        so_type1_is_ti_count = self.type1.invoice_status_ti_so_count
        sale_picking = sale.picking_ids
        for move in sale_picking.move_ids_without_package:
            move.move_line_ids.write({"qty_done": move.sale_line_id.product_uom_qty})
        sale_picking._action_done()
        self.assertEqual(
            self.type1.invoice_status_no_so_count, so_type1_is_no_count - 1
        )
        self.assertEqual(
            self.type1.invoice_status_ti_so_count, so_type1_is_ti_count + 1
        )

    def _create_sale(self, line_products):
        """Create a sale order.
        ``line_products`` is a list of tuple [(product, qty)]
        """
        lines = []
        for product, qty in line_products:
            line_values = {
                "name": product.name,
                "product_id": product.id,
                "product_uom_qty": qty,
                "product_uom": product.uom_id.id,
                "price_unit": 100,
            }
            lines.append((0, 0, line_values))
        sale = self.so_obj.create(
            {
                "partner_id": self.partner1.id,
                "type_id": self.type1.id,
                "order_line": lines,
            }
        )
        return sale
