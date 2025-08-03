from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalICUBooking(models.Model):
    _name = 'hospital.icu.booking'
    _description = 'ICU Bed Booking'
    _order = 'start_datetime desc'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    bed_id = fields.Selection([
        ('A1', 'ICU Bed A1'),
        ('A2', 'ICU Bed A2'),
        ('A3', 'ICU Bed A3'),
        ('A4', 'ICU Bed A4'),
        ('A5', 'ICU Bed A5'),
        ('A6', 'ICU Bed A6'),
    ], string='ICU Bed', required=True)

    start_datetime = fields.Datetime(string='Start Time', default=fields.Datetime.now)
    end_datetime = fields.Datetime(string='End Time')
    notes = fields.Text(string='Notes')
   # bed_image = fields.Image(string="ICU Bed Image", default=lambda self: self._get_default_image())

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancel','Cancelled'),
    ], string='State', default='draft')

    def action_confirm(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'confirmed'  # Change the state to 'confirmed'

    def action_ongoing(self):
        """ This method is called when the 'Ongoing' button is clicked """
        for record in self:
            if record.state == 'confirmed':
                record.state = 'ongoing'  # Change the state to 'ongoing'

    def action_complete(self):
        """ This method is called when the 'Complete' button is clicked """
        for record in self:
            if record.state == 'ongoing':
                record.state = 'completed'  # Change the state to 'completed'

    def action_cancel(self):
        """ This method is called when the 'Draft' button is clicked (to revert the booking back to draft) """
        for record in self:
            if record.state == 'completed':
                record.state = 'cancel'  # Change the state to 'draft'

    def _get_default_image(self):
        # Returning the image directly from a static folder path
        return open('custom_addons/hospital_management_system/static/description/bed1.png', 'rb').read()

    def action_save_icu_save(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'ICU Bookings',
            'res_model': 'hospital.icu.booking',
            'view_mode': 'list,form',
            'target': 'current',
        }
