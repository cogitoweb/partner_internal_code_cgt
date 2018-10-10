# -*- coding: utf-8 -*-
{
    'name': "Partner Internal Code",
    'summary': "Partner Internal Code",

    'description': """
        Partner Internal Code
    """,

    'author': "Cogito",
    'license': "OPL-1",
    'website': "https://www.cogitoweb.it",

    'category': 'Tools',
    'version': '10.0.1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'sale'
    ],

    # always loaded
    'data': [
        'data/ir_sequence.xml',
        'views/res_partner.xml'
    ],

    # only loaded in demonstration mode
    'demo': [ ],
}