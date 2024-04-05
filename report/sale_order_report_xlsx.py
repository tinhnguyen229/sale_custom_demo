from odoo import models, _


class SaleOrderReportXlsx(models.AbstractModel):
    # _name = 'report.module_name.report_name'
    _name = 'report.sale_custom_demo.action_report_saleorder_xlsx_test'
    _description = "Report Sale Order Xlsx"
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, objects):
        print('workbook: ', workbook)
        print('data: ', data)
        print('objects: ', objects)
        for obj in objects:
            sheet = workbook.add_worksheet('sheet1')
            self.generate_header(workbook, sheet)
            self.generate_data(workbook, sheet, objects)
            self.format_xlsx_sheet(sheet)

    def generate_header(self, workbook, sheet):
        big_header = workbook.add_format({'bold': True, 'font_name': 'Times New Roman', 'font_size': 22})
        sub_header = workbook.add_format({'bold': True, 'font_name': 'Times New Roman', 'font_size': 13, 'border': 1})
        sheet.merge_range('A1:C1', 'Danh sach cac don ban hang', big_header)
        sheet.write(1, 0, "Stt", sub_header)
        sheet.write(1, 1, "ID", sub_header)
        sheet.write(1, 2, "Name", sub_header)
        sheet.write(1, 3, "Customer", sub_header)

    def generate_data(self, workbook, sheet, objs):
        row_index = 2
        orders = self.env['sale.order'].sudo().search([])
        data_format = workbook.add_format({'font_name': 'Times New Roman', 'font_size': 13, 'num_format': '@', 'right': 1, 'bottom': 3})
        for order in orders:
            sheet.write(row_index, 0, row_index - 1, data_format)
            sheet.write(row_index, 1, order.id, data_format)
            sheet.write(row_index, 2, order.name, data_format)
            sheet.write(row_index, 3, order.partner_id.name, data_format)
            row_index += 1

    def format_xlsx_sheet(self, sheet):
        sheet.set_column(0, 0, 11)
        sheet.set_column(1, 1, 22)
        sheet.set_column(2, 2, 35)
