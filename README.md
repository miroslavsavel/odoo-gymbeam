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

```<record id="viewcustom_employee" model="ir.ui.view">
            <field name="name">viewcustom.employee</field>
            <field name="model">hr.employee</field>
            <field name="inherit_id" ref="hr.view_employee_form"/>
            <field name="arch" type="xml">
                <field name="work_email" position="after">
                    <field name="i_love_gb"/>
                </field>
            </field>
        </record>
        .```


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


