from odoo import models, fields

from odoo import api



class HospitalMedicalHistory(models.Model):
    _name = 'hospital.medical.history'
    _description = 'Medical History'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    patient_age = fields.Char(string="Age", related='patient_id.age', store=True)
    patient_name = fields.Char(string="Patient Name", related='patient_id.name', store=True)
    diagnosis_date = fields.Date(string="Diagnosed On")
    condition = fields.Char(string="Condition")
    notes = fields.Text(string="Details")
    test_type = fields.Selection([
        ('blood', 'Blood Test'),
        ('cardiac', 'Cardiac Test'),
        ('urine', 'Urine Test'),
        ('imaging', 'Imaging'),
        ('rapid', 'Rapid Test'),
    ], string="Test Type")

    test_type_ids = fields.Many2many(
        'hospital.test.type',
        string="Test Types",
        help="Select all applicable test types"
    )

    medicine_line_ids = fields.One2many('hospital.medicine.line', 'history_id', string="Medicines")

    def action_save_patient(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Medical History',
            'res_model': 'hospital.medical.history',
            'view_mode': 'list,form',
            'target': 'current',
        }


