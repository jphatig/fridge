# -*- coding: utf-8 -*-

from odoo import api, fields, models

class FridgeMenu(models.Model):
    _name = 'fridge.menu'
    _description = 'Food menu'

    name = fields.Char(
        string='Name'
    )
    dish_ids = fields.Many2many(
        comodel_name='fridge.dish',
        string='Dishes'
    )
    day = fields.Selection(
        string='Day to eat',
        selection=[
            ('mon', 'Monday'),
            ('tue', 'Tuesday'),
            ('wed', 'Wednesday'),
            ('thu', 'Thursday'),
            ('fri', ' Friday')
        ]
    )
    hour = fields.Integer(
        string='Hour to eat'
    )
    minute = fields.Integer(
        string='Minute to eat'
    )
