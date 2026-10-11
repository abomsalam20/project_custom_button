{   
    'name': 'Custom Button for Project',
    'version': '19.0.1.0.0',
    'license': 'OPL-1',
    'support': 'https://www.github.com/abomsalam20',
    'summary': 'Custom button for project.',
    'author': "SW - Mostafa Abomsalam",
    'category': 'Extra',
    'description': """Project Custom Button""",
    'website': "https://github.com/abomsalam20/project_custom_button",
    'depends': ['base', 'project'],
    'images': [
        'project_custom_button/static/description/project_button_icon.png', 
    ],
    'icon': 'project_custom_button/static/description/project_button_icon.png',
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
