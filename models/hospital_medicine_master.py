# models/medicine_master.py
from odoo import models, fields

class HospitalMedicineMaster(models.Model):
    _name = 'hospital.medicine.master'
    _description = 'Medicine Master'

    name = fields.Char(string="Medicine Name", required=True)
