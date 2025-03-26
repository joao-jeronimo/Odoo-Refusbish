{
    'name': 'Refurbisher',
    'version': 'ODOO_RELEASE.0.1',
    'author': 'João Jerónimo',
    'data': [
        'views_and_actions.xml',
        'ir.model.access.csv',
    ],
    'depends': [
        'base',
        # Kanban for attachment preview:
        'mail',
        ],
    'auto_install': False,
}
