{
  	'name': 'Rolans Real Estate',
	'version': '0.1',
	'summary': 'Tutorial Project',
	'description': """
		This module is for the Odoo developer's tutorial.
	""",
	'category': 'Tutorials',
	'license': 'LGPL-3',
	'depends': [
		'base_setup',
	],
	'data': [
		'security/ir.model.access.csv',
		'views/estate_property_views.xml',
		'views/property_type_views.xml',
		'views/property_tag_views.xml',
		'views/estate_menus.xml',
	],
	'installable': True,
	'application': True,
	'auto_install': False,

}
