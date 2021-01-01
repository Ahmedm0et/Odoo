from odoo import models, fields ,api
from datetime import datetime


class log(models.Model):
    _name="log.record"
    patient_id= fields.Many2one("hms.patient")
    # createdby= fields.Char()
    date= fields.Date(default=datetime.today())
    description= fields.Text()


