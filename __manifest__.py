# -*- coding: utf-8 -*-
{
    'name': "i4survey",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "BU1 - DTT",
    'website': "http://dtt.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'web', 'mail', 'link_tracker', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/header.xml',
        'views/homepage.xml',
        'views/icon.xml',
        'views/i4survey_view.xml',
        'views/i4survey_mail_template.xml',
        'views/result_message.xml',
        'views/data_group.xml',
        'views/thank_you.xml',
        'views/crm_lead_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}