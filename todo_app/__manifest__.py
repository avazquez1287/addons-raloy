# -*- coding: utf-8 -*-
{
    'name': 'To-Do Application',
    'description': 'Controlar las tareas personales',
    'depends': ['base'],
    'application': True,
    'website': 'www.raloylubricantes.mx',
    'author': 'Arturo Vazquez',

    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/res_partner_view.xml',
        'views/index_template.xml',
    ],
}