from odoo import models, fields


class Departments(models.Model):
    _name= "hms.department"
    name=fields.Char()
    capacity= fields.Integer()
    is_opened= fields.Boolean('is_opened')
    patients= fields.One2many("hms.patient","department_id")

