{
    'name': 'POS Sale',
    'version': '1.0',
    'category': 'Open',
    'sequence': 1,
    'summary': 'Invoiced Sale Order',
    'description': """
Show invoiced sale order in POS Front Screen  
====================================================


Dashboard for Activity  will include:
-------------------------------

""",
    'author': 'Atul Jain',
    'website': 'http://www.netbeam.in',
    'depends': [
        'sale',
        'purchase',
        'point of sale'
        'mail',
    ],
    'data': [
        'sale_pos_view.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
