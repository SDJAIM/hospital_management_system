from odoo import models, fields

class HospitalMedicineMaster(models.Model):
    _name = 'hospital.medicine.master'
    _description = 'Master List of Medicines'

    name = fields.Char(string='Medicine Name', required=True, unique=True)
