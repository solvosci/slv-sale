# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo.tests import TransactionCase


class TestSearch(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Test partner"})
        cls.product_bulk = cls.env["product.product"].create({
            "name": "Bulk Product",
            "type": "product",
            "tracking": "none",
            "sale_ok": True,
        })
        cls.product_sn = cls.env["product.product"].create({
            "name": "S/N Product",
            "type": "product",
            "tracking": "serial",
            "sale_ok": True,
        })

    def test_sale_stock_sn_single(self):
        so = self.env["sale.order"].create({
            "partner_id": self.partner.id,
            "order_line": [
                (0, 0, {"product_id": self.product_bulk.id, "product_uom_qty": 2.0}),
                (0, 0, {"product_id": self.product_sn.id, "product_uom_qty": 3.0}),
            ]
        })
        so.action_confirm()

        # S/N product new behavior: one move line per quantity, with a
        #  different description such "My Product Name #1", "My Product Name #2",
        #  and so on 
        prod_sn_sm_ids = so.order_line.filtered(
            lambda x: x.product_id == self.product_sn
        ).move_ids
        self.assertEqual(len(prod_sn_sm_ids), 3)
        self.assertTrue(all(
            qty == 1.0 for qty in prod_sn_sm_ids.mapped("product_uom_qty")
        ))
        self.assertTrue(all(
            ("%s #" % move.product_id.name) in move.description_picking
            for move in prod_sn_sm_ids
        ))

        # Bulk product keeps standard behavior
        prod_bulk_sm_ids = so.order_line.filtered(
            lambda x: x.product_id == self.product_bulk
        ).move_ids
        self.assertEqual(len(prod_bulk_sm_ids), 1)
        self.assertEqual(prod_bulk_sm_ids.product_uom_qty, 2.0)

        # TODO update SO line quantity test 
