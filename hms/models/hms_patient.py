from operator import truediv
from typing import Self

from odoo import fields,models, api
from datetime import date

from odoo.orm.types import ValuesType


class HmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = 'first_name'

    first_name = fields.Char(required = True)
    last_name = fields.Char(required = True)
    birthdate = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')])
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    age = fields.Integer(compute="calc_age")
    department_id = fields.Many2one("hms.department",string = "Department")
    department_capacity = fields.Integer(related="department_id.capacity")
    doctors_ids = fields.Many2many(comodel_name="hms.doctor")
    log_ids = fields.One2many("hms.patient.log","patient_id")
    states = fields.Selection([("Good","Good"),("Undetermined","Undetermined"),("Fair","Fair"),("Serious","Serious")]
                              , default="Undetermined", string="State")

    @api.depends('birthdate')
    def calc_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = date.today().year - rec.birthdate.year
            else:
                rec.age = 0

    @api.onchange("age")
    def pcr_check(self):
        if self.birthdate:
            if self.age<30:
                self.pcr = True
                return {
                    'warning': {
                        'title': 'warning',
                        'message': 'PCR field has been checked because age is less than 30'
                    }
                }
            else:
                self.pcr = False
                return {}

    @api.model
    def create(self, vals):
        record = super().create(vals)

        self.env["hms.patient.log"].create({"description":f"Patient created with state {record.states}" , "patient_id":record.id})
        return record

    def write(self,vals):
        for rec in self:
            if "states" in vals and rec.states != vals["states"]:
                self.env["hms.patient.log"].create(
                    {"description":f"Patient state changed to {vals['states']} ", "patient_id": rec.id})
        return super().write(vals)
