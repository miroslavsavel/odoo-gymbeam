

from odoo import api,models, fields
import xlrd
import base64

class custom_info(models.Model):
    _inherit = 'hr.employee'        # inherit from existing model https://www.youtube.com/watch?v=z1Tx7EGkPy0&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=12
    #task 1
    #NISS = fields.Char(string="NISS : ", required=True)
    #NISS = fields.Boolean(default=True, required=True)
    #NISS = fields.Boolean(string="I love gymbeam")
    # NISS = fields.Char(string="NISS : ", required=True)
    # nove_pole = fields.Char(string="nove_pole : ", required=True)
    i_love_gb= fields.Boolean(default=True, required=True)

    #task 2
    salary = fields.Integer(string='Salary in netto')
    tax = fields.Integer(string='Tax')
    # total_salary = fields.Integer(string='Salary + tax')
    # computed fields and onchanges
    # https://www.odoo.com/documentation/15.0/developer/howtos/rdtraining/09_compute_onchange.html
    total_salary = fields.Float(compute='_compute_total')

    @api.depends('salary', 'tax')
    def _compute_total(self):
        for record in self:
            record.total_salary = record.salary + record.tax

    #task 3
    special_phone = fields.Char(string="special_phone : ", required=False)

    @api.model
    def create(self, vals):
        if not vals.get('special_phone'):
            vals['special_phone'] = '0901123456'
        return super(models.Model, self).create(vals)


    # task 4
    # employee_contacts = fields.Binary(string='Employee contact magic field' )

    # file = fields.Binary(string='File', attachment=True, store=True)
    # file_name = fields.Char('File name')
    

    employee_contacts = fields.Binary(string="Employee contacts")
    file_name = fields.Char(string="File Name")

    #import xls file button
    @api.model
    def import_xls_action(self):
        #Decode data
        data = base64.b64decode(self.employee_contacts)
        #Save file
        with open('/tmp/' + self.file_name, 'wb') as file:
            file.write(data)
        xl_workbook = xlrd.open_workbook(file.name)
        sheet_names = xl_workbook.sheet_names()
        xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
        #Number of columns
        num_cols = xl_sheet.ncols
        #Extract headers from xls file
        headers = []
        for col_idx in range(0, num_cols):
            cell_obj = xl_sheet.cell(0, col_idx)
            headers.append(cell_obj.value)
        #Read xls file and build array of dictionary
        import_data = []
        for row_idx in range(1, xl_sheet.nrows):    # Iterate through rows
            row_dict = {}
            for col_idx in range(0, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                row_dict[headers[col_idx]] = cell_obj.value
            import_data.append(row_dict)
        #  #Browse result and create instance of the contacts model
        for row in import_data:
            email = self.env['res.email'].search([('name','=',row['email'])])
            subject = self.env['res.subject'].search([('name','=',row['subject'])])
            # how to save it to odoo DB?