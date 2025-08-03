from odoo import models, fields
from odoo import api, SUPERUSER_ID


class HospitalMedicineLine(models.Model):
    _name = 'hospital.medicine.line'
    _description = 'Medicine Prescription Line'

    history_id = fields.Many2one('hospital.medical.history', string="Medical History")
    medicine_name = fields.Many2one('hospital.medicine.master', string="Medicine", required=True)

    # medicine_id = fields.Many2one(
    #     'medicine.master',
    #     string='Medicine',
    #     required=True,
    #     ondelete='restrict',
    #     help='Select or create a medicine'
    # )
    dosage = fields.Char(string="Dosage")
    morning_before = fields.Boolean(string="Morning Before Food")
    morning_after = fields.Boolean(string="Morning After Food")
    afternoon_before = fields.Boolean(string="Afternoon Before Food")
    afternoon_after = fields.Boolean(string="Afternoon After Food")
    night_before = fields.Boolean(string="Night Before Food")
    night_after = fields.Boolean(string="Night After Food")
