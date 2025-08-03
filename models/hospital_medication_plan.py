from odoo import models, fields,api


class HospitalMedicationPlan(models.Model):
    _name = 'hospital.medication.plan'
    _description = 'Medication Plan'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    medicine_name = fields.Char('Medication Name')
    medication_count = fields.Integer('Medication Count')
    doctor_id = fields.Many2one('hospital.patient', string="Doctor")  # Add if needed
    bed_id = fields.Many2one('hospital.icu.bed', string="ICU Bed")
    bed_patient_name = fields.Char(string="Patient in Bed", related='bed_id.patient_id.name', store=True)

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string="State", default='draft')

    # Medication lines field: links to the medication line model
    medication_line_ids = fields.One2many('hospital.medication.line', 'patient_id', string='Medications')

    # Instructions for the plan
    note = fields.Text(string="Instructions")

    # Computed field for displaying medication summary

