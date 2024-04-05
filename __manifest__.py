{
    'name': "Sale Custom Demo",
    'version': '1.0',
    'depends': ['sale', 'report_xlsx'],
    'author': "TinhNN",
    'category': 'Category',
    'description': """
        Odoo v17
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',

        # 'views/product_template_view.xml',

        'report/sale_order_report.xml',
        'report/sale_order_report_wizard.xml',
        'report/sale_order_report_xlsx.xml',
        'report/sale_order_report_xlsx_wizard.xml',

        'wizards/sale_order_wizard.xml',
        'wizards/sale_order_xlsx_wizard.xml',
    ],
}