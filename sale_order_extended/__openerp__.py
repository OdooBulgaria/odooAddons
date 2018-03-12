# -*- coding: utf-8 -*-
{
    'name': "Extended Sale Orders",

    'summary': """
        Module which extends the sale-order-workflow to not loose Quotations on getting an order.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jörn Mankiewicz",
    'website': "https://github.com/jmankiewicz/odooAddons",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '8.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_order_revision', 'sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/sale_sequence.xml',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
