# -*- coding: utf-8 -*-

{
    "name": "Fridge",
    "version": "14.0.1.0.1",
    "author": "Jhair Patiño",
    "license": "AGPL-3",
    "website": "N/A",
    "category": "Inventory",
    "depends": ['base', 'product'],
    "data": [
        # Security
        "security/ir.model.access.csv",
        # Views
        "views/menu.xml",
        "views/dish.xml",
        "views/product.xml",
        # Menus
        "views/menu/root.xml"

    ],
    "application": True,
    "installable": True,
}
