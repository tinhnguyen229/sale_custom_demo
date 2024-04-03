from odoo import models, fields, api
import datetime

class SaleOrderWizard(models.TransientModel):
    _name = 'custom.sale.order.wizard'

    user_id = fields.Many2one('res.users', string="User")
    date_from = fields.Date(default=datetime.datetime.now())
    date_to = fields.Date(default=datetime.datetime.now())

    def print_pdf_report(self):
        users = self.env['res.users'].sudo().search([])
        user_datas = []
        for user in users:
            user_datas.append({
                'name': user.name,
                'login': user.login,
                'company': user.company_id.name,
                'state': user.state
            })

        data = {
            'data': {
                'name': self.user_id.name,
                'date_from': self.date_from.strftime('%Y-%m-%d'),
                'date_to': self.date_to.strftime('%Y-%m-%d'),
            },
            'user_datas': user_datas
        }
        # return self.env.ref('xml_id of template', data=data)
        return self.env.ref('sale_custom_demo.action_report_saleorder_test_template_wizard_test').report_action(self, data=data)
