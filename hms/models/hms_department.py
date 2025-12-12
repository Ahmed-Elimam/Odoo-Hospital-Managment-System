from odoo import fields,models,api

class HmsDepartment(models.Model):
    _name = "hms.department"
    _rec_name = "name"

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_ids = fields.One2many(comodel_name="hms.patient",inverse_name="department_id", string="Department Patients")
