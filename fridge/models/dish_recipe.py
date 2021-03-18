# -*- coding: utf-8 -*-

from odoo import api, fields, models

class FridgeDishRecipe(models.Model):
    _name = 'fridge.dish.recipe'
    _description = 'Food dish recipes specifiying products and quants'

    dish_id = fields.Many2one(
        comodel_name='fridge.dish',
        string='Dish'
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        required=True
    )
    quant = fields.Integer(
        string='Quant',
        required=True
    )
    uom = fields.Many2one(
        comodel_name='uom.uom',
        string='UoM',
        required=True
    )
