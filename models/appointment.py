from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Patient Appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('res.users', string="Doctor", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", default=fields.Datetime.now)
    reason = fields.Text(string="Reason for Visit")
    fee = fields.Float(string='Appointment Fee')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default='draft', tracking=True)

    def action_confirm(self):
        for rec in self:
         rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
         rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_save_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'target': 'current',
        }

    def action_go_back(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'target': 'current',
        }





appointment_type = fields.Selection([
    ('checkup', 'General Checkup'),
    ('followup', 'Follow-up'),
    ('emergency', 'Emergency'),
], string="Appointment Type")

duration = fields.Float(string="Duration (hrs)")

notes = fields.Html(string="Doctor's Notes")

is_first_visit = fields.Boolean(string="First Visit")




