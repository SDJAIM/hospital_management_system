from odoo import http
from odoo.http import request
from datetime import datetime, timedelta
import json

class WebsiteAppointment(http.Controller):
    @http.route('/appointment', type='http', auth="public", website=True)
    def appointment_booking(self, **kw):
        services = request.env['product.product'].search([
            ('type', '=', 'service'),
            ('hospital_service', '=', True)
        ])
        doctors = request.env['res.users'].search([
            ('is_doctor', '=', True)
        ])
        
        min_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        
        return request.render('hospital_management_system.appointment_booking', {
            'services': services,
            'doctors': doctors,
            'min_date': min_date,
            'time_slots': [
                '09:00 AM', '10:00 AM', '11:00 AM',
                '02:00 PM', '03:00 PM', '04:00 PM'
            ]
        })

    @http.route('/appointment/submit', type='http', auth="public", website=True)
    def submit_appointment(self, **post):
        appointment = request.env['hospital.appointment'].create({
            'patient_id': request.env.user.partner_id.id,
            'doctor_id': int(post.get('doctor_id')),
            'appointment_date': post.get('appointment_date') + ' ' + post.get('time_slot'),
            'reason': post.get('notes'),
            'insurance_docs': post.get('insurance_docs'),
        })
        
        return request.redirect(f'/appointment/confirmation/{appointment.id}')

    @http.route('/appointment/confirmation/<int:appointment_id>', type='http', auth="public", website=True)
    def appointment_confirmation(self, appointment_id, **kw):
        appointment = request.env['hospital.appointment'].browse(appointment_id)
        return request.render('hospital_management_system.appointment_confirmation', {
            'appointment': appointment
        })
