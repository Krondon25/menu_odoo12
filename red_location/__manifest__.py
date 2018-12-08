# -*- coding: utf-8 -*-
# Copyright 2018 AITIC - Rondón Kristian  <rondonkristian@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
{
    'name': "location",
    'description': """
        Associate a project with the tickets.
    """,
    'author': "AITIC",
    'website': "http://aitic.com.ar/",
    'category': 'Helpdesk',
    'version': '12.0.1.0.0',
    'depends': ['crm'],
    'data': [
        'views/location_view.xml',
        'views/res_partner_view.xml',
        'views/statistical_view.xml',
    ],
}
