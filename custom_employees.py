

from odoo import models, fields
class custom_info(models.Model):
    _inherit = 'hr.employee'
    #NISS = fields.Char(string="NISS : ", required=True)
    #NISS = fields.Boolean(default=True, required=True)
    #NISS = fields.Boolean(string="I love gymbeam")
    NISS = fields.Char(string="NISS : ", required=True)

