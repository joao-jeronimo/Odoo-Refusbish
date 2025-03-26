{   'name': 'Social posting',
    'description': "Models and tools for composing posts for social networks.",
    'version': 'ODOO_RELEASE.0.1',
    'author': 'João Jerónimo',
    'data': [
        'views_and_actions.xml',
        'ir.model.access.csv',
        ],
    'demo': [
        'demo.xml',
        ],
    'depends': [
        'base',
        # Kanban for attachment preview:
        'mail',
        ],
    'auto_install': False,
}
