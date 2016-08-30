{
    'name': 'Sales Team Invoice Amount in India Format in Kanban View',
    'category': 'sale',
    'description': """
This module displays Sales Team Invoice Target and Invoiced this Month with Crores/Lakhs/Thousnads instead of Millions in Kanban View.
Decimals also Possible to Show.
""",
    'author': 'Murali Krishna Reddy',
    'website': 'http://www.credativ.in',
    'sequence':0,
    'version': '1.0',
    'depends': ['web_kanban_gauge','sales_team'],
    'images':['images/gauge1.png'],
    'data' : [
        'views/web_kanban_gauge_ind.xml',
        'views/res_company_view.xml',
        'views/sales_team_view.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}


