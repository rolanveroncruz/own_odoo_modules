{
    'name': 'Argotek Salesforce',
    'version': '0.1',
    'author': 'RolanVC',
    'summary': 'App for Salesforce itinerary and expenses',
    'description': """
    This module is for Argotek's Sales Manager to track expenses and itineraries.
	""",
    'category': 'Argotek',
    'license': 'LGPL-3',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/weekly_sales_plan_form_view.xml',
        'views/weekly_sales_plan_actions.xml',
        'views/weekly_sales_plan_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
