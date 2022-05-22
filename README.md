# Case Study - Odoo developer

## 1. TASK: Create a new boolean field i_love_gb on the Employee screen after the work_email field.
    - Find out how the model of employee is named.
    - Find out how the view of the employee form is named. (hint: find out how developer
    mode is activated in Odoo, then via this menu item ‘edit view:form’ structure and name/id
    of the view can be found, there are also other ways)
    - Override employee model/view to add new field
    - Install your new module

## DONE

![alt text](https://i.ibb.co/vDGSzG6/1.png)

### solution
from odoo import api,models, fields
class custom_info(models.Model):
    _inherit = 'hr.employee' 
    i_love_gb= fields.Boolean(default=True, required=True)

create view viewcustom_employee


## 2. TASK: Create 3 new Integer fields salary, tax and total_salary.
-  Field total_salary should be automatically set to value salary + tax. New fields should be after the address field on the Private information tab. (hint: onchange, depends, compute...)

## DONE
![alt text](https://i.ibb.co/mF0wymW/2.png)

### solution
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


## 3. TASK: Replace phone field with new field special_phone.
- On save action of the employee record, check if the field is empty, if it is empty, set the default value of the field to “0901123456”.

## DONE
![after save](https://i.ibb.co/kc7BPyJ/3b.png)

### solution
#task 3
    special_phone = fields.Char(string="special_phone : ", required=False)

    @api.model
    def create(self, vals):
        if not vals.get('special_phone'):
            vals['special_phone'] = '0901123456'
        return super(models.Model, self).create(vals)

## 4. TASK: create import field for excel, read from that file, add button, sent email
● This field will be visible only if i_love_gb is set to True.
● Create an excel file with 2+ lines. First column will be some random mail (or existing),
second one will be some random text value.
● Upload this excel into a binary field.
● Create a new button Send emails next to the Launch plan button. After clicking on the
button Odoo will send an email with text Welcome in GymBeam to the email addresses
in the first column. Subject of the email will be value from the second column.
As an email server, simple gmail mail can be used: Send and Receive Emails in Odoo
If no correct outgoing email server is set, Odoo will store failed emails and they can be
opened in GUI, find out where (developer mode is needed to be activated).
● Bonus: Transfer this functionality to a wizard. Wizard can be opened via button click on
employee form or from any place from the menu.

## PARTIALLY DONE

# TODO
    - sent email after button click

![button](https://i.ibb.co/bWk7bpM/4.png)

### solution
task 4
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