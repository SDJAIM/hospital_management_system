from odoo import models, fields

class HospitalDoctorNote(models.Model):
    _name = 'hospital.doctor.note'
    _description = 'Doctor Note'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('res.users', string="Doctor", required=True)
    note_date = fields.Date(string="Date", default=fields.Date.today)
    notes = fields.Text(string="Notes")

    def action_save_doctor_note(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Doctor Notes',
            'res_model': 'hospital.doctor.note',
            'view_mode': 'list,form',
            'target': 'current',
        }

