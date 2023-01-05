# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Pen Academy Management',
    'version' : '1.0',
    'summary': 'Pen Academy management software',
    'sequence': -100,
    'description': """
Pen Academy management software
    """,
    'category': 'Productivity',
    'author': 'Eng: Asmaa Sobhy',
    'website': 'https://www.asmaa.tech',
    'depends' : ['partner_autocomplete',
                 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/session_wizard_view.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/partner_view.xml',

        'report/session_details_template.xml',
        'report/report.xml',






    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
