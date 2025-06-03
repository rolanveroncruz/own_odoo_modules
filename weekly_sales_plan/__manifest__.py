{
    'name': 'Weekly Sales Plan',
    'version': '0.1',
    'author': 'RolanVC',
    'summary': 'An app for Weekly Sales Plannging',
    'description': """
    This is an app for Weekly Sales Plannging, to track client visits and expenses.
	""",
    'category': 'Argotek',
    'license': 'LGPL-3',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/weekly_sales_plan_form_view.xml',
        'views/weekly_sales_plan_list_view.xml',
        'views/weekly_sales_plan_calendar_view.xml',
        'views/weekly_sales_plan_actions.xml',
        'views/weekly_sales_plan_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
