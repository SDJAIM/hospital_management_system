# models/test_type.py
from odoo import models, fields

class HospitalTestType(models.Model):
    _name = 'hospital.test.type'
    _description = 'Test Type Master'

    name = fields.Char(string="Test Type", required=True)
