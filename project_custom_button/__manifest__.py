{   
    'name': 'Custom Button for Project',
    'version': '19.0.1.0.0',
    'license': 'OPL-1',
    'support': 'https://www.github.com/abomsalam20',
    'summary': 'Custom button for project.',
    'author': "SW - Mostafa Abomsalam",
    'category': 'Extra',
    'description': """<p>Project Custom Button Module</p>
<p>This module adds custom buttons to the project management interface.</p>""",
    'website': "https://github.com/abomsalam20/project_custom_button",
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'icon': 'static/description/icon.png',
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
}