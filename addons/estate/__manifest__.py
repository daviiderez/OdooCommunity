# -*- coding: utf-8 -*-

{
    'name': 'Estate Application',
    'application': True,
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/estate_tree_views.xml',
        'views/estate_form_views.xml',
        'views/estate_search_view.xml',
        'views/estate_type_menu.xml',
        'views/estate_tags_menu.xml'
    ]
}