# -*- coding: utf-8 -*-

from odoo import api, fields, models

class FridgeDish(models.Model):
    _name = 'fridge.dish'
    _description = 'Food dishes using products'

    name = fields.Char(
        string='Name'
    )
    recipe_ids = fields.One2many(
        comodel_name='fridge.dish.recipe',
        inverse_name='dish_id',
        string='Ingredients'
    )
    instructions = fields.Html(
        string='Instructions'
    )
