from odoo import models, fields, api, _
from datetime import date
import re
from odoo.exceptions import  UserError

class Hospital(models.Model):
    _name="hms.patient"
    _rec_name='first'

    # def age_calc(self):
    #         self.age=(datetime.today().date() - datetime.strptime(
    #             self.date_of_birth,'%Y-%m-%d').date()) // timedelta(days=365)

    first = fields.Char(required=True)
    last = fields.Char()
    email =fields.Char()
    birth = fields.Date()
    age = fields.Integer(compute="calc_age",store=True)
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(
        [('A+',"A+"),
         ('A-',"A-"),
         ('AB+',"AB+"),
         ('AB-',"AB-"),
         ('B+',"B+"),
         ('B-',"B-"),
         ('O+',"O+"),
         ('O-',"O-"),
        ]
    )
    pcr= fields.Boolean('PCR')
    image= fields.Binary()
    address= fields.Text()


    state= fields.Selection(
        [('u',"Undetermined"),
         ('g',"Good"),
         ('f',"Fair"),
         ('s',"Serious")
        ],default='u'    )

    department_id= fields.Many2one("hms.department")
    capacity= fields.Integer(related="department_id.capacity")
    doctor_id= fields.Many2many("hms.doctor")
    log_id= fields.One2many("log.record","patient_id")

    @api.onchange("age")
    def on_change_age(self):
        if self.age and self.age < 30:
            pcr = True
            return {
                "warning":{
                    "title": "notice",
                    "message":"PCR has been checked"
                }}


    def Undetemined(self):
        for patient in self:
            patient.state='u'
            self.env['log.record'].create({
                'description': 'Patient state is Undetemined',
                'patient_id': patient.id
            })

    def Set_Good(self):
        for patient in self:
            patient.state='g'
            self.env['log.record'].create({
                'description': 'Patient state is Good',
                'patient_id': patient.id
            })

    def Set_Fair(self):
        for patient in self:
            patient.state='f'
            self.env['log.record'].create({
                'description': 'Patient state is Fair',
                'patient_id': patient.id
            })

    def Set_Serious(self):
        for patient in self:
            patient.state = 's'
            self.env['log.record'].create({
                'description': 'Patient state is Serious',
                'patient_id': patient.id
            })

    _sql_constraints=[
        ('uniqu_mail','UNIQUE(email)','Email already exist..')
    ]

    @api.constrains("email")
    def checkMail(self):
        regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if self.email:
            if not re.search(regex,'self.email'):
                raise UserError("Not valid mail")

    @api.depends('birth')
    def calc_age(self):
        for rec in self:
            if rec.birth:
                rec.age=date.today().year - rec.birth.year





