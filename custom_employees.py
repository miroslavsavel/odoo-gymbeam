

from odoo import api,models, fields
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
    special_phone = fields.Char(string="special_phone : ", required=True)
