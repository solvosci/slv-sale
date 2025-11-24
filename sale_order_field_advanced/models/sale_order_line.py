# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = ['sale.order.line', 'adv.state.mixin']
    _name = 'sale.order.line'

    name = fields.Text(compute='_compute_name', required=False, readonly=False)

    adv_reference = fields.Char()
    adv_is_tailored = fields.Boolean()
    adv_characteristics = fields.Text()
    adv_modification_id = fields.Many2one('sale.order.line.modification')
    adv_note = fields.Text()
    adv_complement_id = fields.Many2one('product.template')
    adv_complement_size = fields.Char()
    adv_complement_group = fields.Char()
    adv_manufacturing_state_id = fields.Many2one('sale.order.line.process.status',
                                                 compute='_compute_adv_manufacturing_state_id', store=True)
    adv_date_order = fields.Datetime(
        related="order_id.date_order",
        store=True,
    )

    adv_product_has_process_control = fields.Boolean(
        related="product_id.categ_id.has_process_control",
    )

    adv_manufacturing_state_name = fields.Char(
        string='Manufacturing State Name',
        related='adv_manufacturing_state_id.name',
    )

    adv_manufacturing_state_decoration = fields.Char(compute='_compute_adv_manufacturing_state_decoration')

    adv_final_state =fields.Boolean(
        related='adv_manufacturing_state_id.final_state',
    )

    adv_unitary_product_price = fields.Float(compute='_compute_adv_unitary_product_price', store=True, readonly=False)

    adv_requested_delivery_date = fields.Date(
        related='order_id.adv_requested_delivery_date',
        string='Requested Delivery Date',
        store=True
    )

    @api.depends("adv_manufacturing_state_id.decoration_color")
    def _compute_adv_manufacturing_state_decoration(self):
        line_with_state = self.filtered(lambda x: x.adv_manufacturing_state_id)
        for line in line_with_state:
            line.adv_manufacturing_state_decoration = line.adv_manufacturing_state_id.decoration_color
        (self - line_with_state).update({"adv_manufacturing_state_decoration": False})

    @api.depends('product_id')
    def _compute_adv_manufacturing_state_id(self):
        initial_state = self.env['sale.order.line.process.status'].search(
            [("initial_default_state", "=", True)], limit=1)
        no_process_state = self.env['sale.order.line.process.status'].search(
            [("no_process_default_state", "=", True)], limit=1)

        for record in self:
            if record.adv_product_has_process_control:
                record.adv_manufacturing_state_id = initial_state
            else:
                record.adv_manufacturing_state_id = no_process_state
                record.clear_fields()

    def recalculate_complement_group(self, result):
        for line in result:
            if line.adv_complement_id:
                line.adv_complement_size = line.complement_size()
                line.adv_complement_group = f"{line.adv_complement_id.name} | {line.adv_complement_size}".strip()

    def clear_fields(self):
        self.update({
            "adv_reference": False,
            "adv_note": False,
            "adv_modification_id": False,
            "adv_characteristics": False,
            "adv_is_tailored": False,
            "adv_complement_id": False,
        })

    @api.depends('product_id')
    def _compute_adv_unitary_product_price(self):
        for line in self:
            line.adv_unitary_product_price = line.price_unit

    def write(self, values):
        result = super(SaleOrderLine, self.sudo()).write(values)
        if 'adv_complement_id' in values or 'name' in values:
            self.recalculate_complement_group(self)
        self.recalculate_unitary_price(values)
        return result

    def create(self, values):
        result = super(SaleOrderLine, self.sudo()).create(values)
        if 'adv_complement_id' in values or 'name' in values:
            self.recalculate_complement_group(self)
        self._compute_name()
        result.recalculate_unitary_price(values)
        return result

    @api.depends('product_id', 'adv_reference', 'adv_characteristics', 'adv_modification_id', 'adv_complement_id')
    def _compute_name(self):
        for line in self:
            parts = [line.product_id.display_name]
            if line.adv_reference:
                parts.append(line.adv_reference)
            if line.adv_characteristics:
                parts.append(line.adv_characteristics)
            if line.adv_modification_id:
                parts.append(line.adv_modification_id.name)
            if line.adv_complement_id:
                parts.append(line.adv_complement_id.name)
            line.name = '\n'.join(filter(None, parts))

    def recalculate_unitary_price(self, values):
        watched_fields = ["adv_complement_id", "adv_modification_id", "adv_unitary_product_price", "qty_delivered_manual", "tax_id", "product_id"]
        manual_created_line = "qty_delivered_manual" in values

        if not any(field in watched_fields for field in values) and not manual_created_line:
            return

        for line in self:
            base_price = line.adv_unitary_product_price or 0.0

            complement_price = 0.0
            if line.adv_complement_id and line.adv_complement_id.exists():
                complement_price = line.adv_complement_id.list_price or 0.0

            modification_price = 0.0
            if line.adv_modification_id and line.adv_modification_id.exists():
                modification_price = line.adv_modification_id.price or 0.0
                modification_price = line.adv_modification_id.currency_id._convert(
                    modification_price,
                    line.order_id.company_id.currency_id,
                    line.order_id.company_id,
                    fields.Date.today()
                )

            line.price_unit = base_price + complement_price + modification_price

    def complement_size(self):
        product_values = self.product_id.product_template_attribute_value_ids.mapped("product_attribute_value_id")
        if product_values:
            equivalence = self.env["product.complement.size"].search([
                ("product_size_ids", "in", product_values.ids),
                ("active", "=", True)
            ], limit=1)

            return equivalence.name if equivalence else None
        return None

    def open_manufacturing_state_wizard(self):
        wizard = self.env['sale.order.line.manufacturing.state.wizard']
        new = wizard.create({
            "line_ids": [(4, line_id) for line_id in self.env.context.get("active_ids", [])],})

        return {
            'name': _('Change Manufacturing State'),
            'res_model': 'sale.order.line.manufacturing.state.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': new.id,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

    def open_complement_tag_state_wizard(self):
        wizard = self.env['sale.order.line.complement.tag.wizard']
        new = wizard.create({
            "line_ids": [(4, line_id) for line_id in self.env.context.get("active_ids", [])],})

        return {
            'name': _('Change Complement And Tag State'),
            'res_model': 'sale.order.line.complement.tag.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': new.id,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
