from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Patient Appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('res.users', string="Doctor", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", default=fields.Datetime.now)
    appointment_slot = fields.Char(string="Time Slot", compute='_compute_time_slot', store=True)
    
    @api.constrains('appointment_date', 'doctor_id')
    def _check_appointment_validity(self):
        for record in self:
            if record.appointment_date:
                # Check minimum booking date (7 days in advance)
                min_date = fields.Datetime.now() + timedelta(days=7)
                if record.appointment_date < min_date:
                    raise ValidationError(_("Appointments must be booked at least 7 days in advance"))
                
                # Check doctor availability
                if record.doctor_id:
                    work_schedule = record.doctor_id.resource_calendar_id
                    if work_schedule:
                        if not work_schedule.check_working_time(
                            start_dt=record.appointment_date,
                            end_dt=record.appointment_date + timedelta(hours=record.duration or 1)
                        ):
                            raise ValidationError(_("Doctor is not available at the selected time"))
    reason = fields.Text(string="Reason for Visit")
    fee = fields.Float(string='Appointment Fee')
    insurance_docs = fields.Binary(string="Insurance Documents")
    insurance_number = fields.Char(string="Authorization Number")
    secretary_notes = fields.Text(string="Secretary Notes")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default='draft', tracking=True)

    @api.depends('appointment_date')
    def _compute_time_slot(self):
        for rec in self:
            if rec.appointment_date:
                rec.appointment_slot = rec.appointment_date.strftime("%I:%M %p")

    def action_submit_for_approval(self):
        for rec in self:
            rec.state = 'pending'

    def action_confirm(self):
        for rec in self:
            if rec.insurance_docs and not rec.insurance_number:
                raise UserError("Authorization number is required for insurance appointments")
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
