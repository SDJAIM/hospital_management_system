# from odoo import models, fields, api
#
# class HospitalICUBookingLine(models.Model):
#     _name = 'hospital.icu.booking.line'
#     _description = 'ICU Booking Line'
#
#     booking_id = fields.Many2one('hospital.icu.booking', string='ICU Booking', required=True, ondelete='cascade')
#     bed_id = fields.Selection('hospital.icu.booking', string='ICU Bed', store=True)
#     patient_id = fields.Many2one('hospital.icu.booking', string='Patient', store=True)
#     state = fields.Selection('hospital.icu.booking', string='State', store=True)
#
