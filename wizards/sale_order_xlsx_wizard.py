import datetime
from odoo import models, fields, _


class SaleOrderReportXlsxWizard(models.TransientModel):
    # _name = 'report.module_name.report_name'
    _name = 'sale.order.xlsx.wizard'

    user_id = fields.Many2one('res.users', string="User")
    date_from = fields.Date(default=datetime.datetime.now())
    date_to = fields.Date(default=datetime.datetime.now())

    def action_generate_xlsx_report(self):
        data = {
            'username': self.user_id.name,
            'date_from': self.date_from.strftime('%Y-%m-%d'),
            'date_to': self.date_to.strftime('%Y-%m-%d'),
        }
        return self.env.ref('sale_custom_demo.report_saleorder_xlsx_test_wizard').report_action(self, data=data)