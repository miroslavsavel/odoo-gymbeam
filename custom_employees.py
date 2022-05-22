

from odoo import models, fields
class custom_info(models.Model):
    _inherit = 'hr.employee'        # inherit from existing model https://www.youtube.com/watch?v=z1Tx7EGkPy0&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=12
    #NISS = fields.Char(string="NISS : ", required=True)
    #NISS = fields.Boolean(default=True, required=True)
    #NISS = fields.Boolean(string="I love gymbeam")
    # NISS = fields.Char(string="NISS : ", required=True)
    # nove_pole = fields.Char(string="nove_pole : ", required=True)
    i_love_gb= fields.Boolean(default=True, required=True)

