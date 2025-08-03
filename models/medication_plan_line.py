from odoo import models, fields,api




class MedicationPlanLine(models.Model):
    _name = 'hospital.medication.plan.line'
    _description = 'Medication Plan Line'

    bed_id = fields.Many2one('hospital.icu.bed', string="ICU Bed")
    bed_patient_name = fields.Char(string="Patient in Bed", related='bed_id.patient_id.name', store=True)
    medicine_name = fields.Char(string='Medicine', required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    duration = fields.Integer(string='Duration (days)')
    dosage = fields.Char(string="Dosage")
    frequency_morning = fields.Boolean(string='Morning')
    frequency_afternoon = fields.Boolean(string='Afternoon')
    frequency_evening = fields.Boolean(string='Evening')
    frequency_night = fields.Boolean(string='Night')
    instruction = fields.Text(string='Instructions')
    medication_line_ids = fields.One2many('hospital.medication.plan.line', 'patient_id',string='Medications')
    note = fields.Text(string="Instructions")

    @staticmethod
    def action_save_medication_line():
        return {
            'type': 'ir.actions.act_window',
            'name': 'Medication Plan Lines',
            'res_model': 'action_medication_plan',
            'view_mode': 'list,form',
            'target': 'current',
        }

    # @api.onchange('bed_id')
    # def _onchange_bed_id(self):
    #     if self.bed_id:
    #         booking = self.env['hospital.icu.booking'].search([
    #             ('bed_id', '=', self.bed_id.id),
    #             ('end_datetime', '=', False)
    #         ], order='start_datetime desc', limit=1)
    #         self.patient_id = booking.patient_id.id if booking else False


