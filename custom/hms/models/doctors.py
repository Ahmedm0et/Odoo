from odoo import models, fields

class Doctors(models.Model):
    _name= "hms.doctor"
    _rec_name='first'

    first=fields.Char(required=True)
    last=fields.Char(required=True)
    image= fields.Binary()
    department_id= fields.Many2many("hms.department")