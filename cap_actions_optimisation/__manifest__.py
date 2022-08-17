# -*- coding: utf-8 -*-
{
    'name': "cap_actions_optimisation",

    'summary': """
        optimisation d'actions auto""",

    'description': """
        optimisation d'actions auto
    """,

    'author': "captivea-agi",
    'website': "http://www.captivea.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_automation'],

    # always loaded
    'data': [
        'views/ir_actions_server.xml',
        'views/base_automation.xml',
    ],
    # only loaded in demonstration mode
    'application': False,
}