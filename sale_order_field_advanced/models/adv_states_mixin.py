# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


from odoo import models, fields

class AdvStateMixin(models.AbstractModel):
    _name = 'adv.state.mixin'
    _description = 'Advanced States Mixin'

    TAG_STATE_SELECTION = [
        ('pending', 'Pending'),
        ('tagged', 'Tagged'),
    ]

    COMPLEMENT_STATE_SELECTION = [
        ('pending', 'Pending'),
        ('sent', 'Sent to Manufacture'),
        ('manufactured', 'Manufactured'),
    ]

    adv_tag_state = fields.Selection(
        TAG_STATE_SELECTION,
        string='Tag State',
        default='pending'
    )

    adv_complement_state = fields.Selection(
        COMPLEMENT_STATE_SELECTION,
        string='Complement Fabrication State',
        default='pending'
    )
