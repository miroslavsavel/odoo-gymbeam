# -*- coding: utf-8 -*-
{
    'name': 'My custom module gymbeam',
    'version': '1.0',
    'category': '',
    'sequence': 5,
    'summary': 'Pridanie noveho fieldu do modulu employee',
    'description': "Modification of employee form",
    'website': 'https://github.com/miroslavsavel',
    'depends':['base','hr',],
    'data': [
#    
                'views/custom_employees_view.xml',
            ],
    'demo': [
        '',
    ],
    'css': [''],
    'installable': True,
    'application': False,
    'auto_install': False
}