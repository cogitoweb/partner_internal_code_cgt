# -*- coding: utf-8 -*-
{
    'name': "Partner Internal Code",
    'summary': "Partner Internal Code",

    'description': """
        Partner Internal Code, based on https://github.com/ingadhoc/partner/tree/9.0/partner_internal_code
    """,

    'author': "CogitoWeb",
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