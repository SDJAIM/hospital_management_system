from odoo import models, fields, api

class MedicationPlan(models.Model):
    _name = 'hospital.medication.plan'
    _description = 'Medication Plan'
    _order = 'start_date desc'

    name = fields.Char(string='Plan Reference', required=True, copy=False, readonly=True, default='New')
    medicine_name = fields.Char(string='Medicine', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('res.users', string='Prescribed By', default=lambda self: self.env.user)
  #  prescription_id = fields.Many2one('hospital.prescription', string='Linked Prescription')
    medication_line_ids = fields.One2many('hospital.medication.plan.line', 'patient_id', string='Medications')
    dosage = fields.Char(string='Dosage')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date')
    medication_count = fields.Integer(string="Medication Count", compute="_compute_medication_count")

    @api.depends('medication_line_ids')
    def _compute_medication_count(self):
        for record in self:
            record.medication_count = len(record.medication_line_ids)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='draft', string='Status')

    frequency = fields.Selection([
        ('daily', 'Daily'),
        ('twice_a_day', 'Twice a Day'),
        ('thrice_a_day', 'Thrice a Day'),
        ('weekly', 'Weekly'),
    ], string='Frequency')

    instructions = fields.Text(string='Instructions')
    note = fields.Text(string='Doctor Instructions')

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', 'New') == 'New':
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hospital.medication.plan') or 'New'
    #     return super(MedicationPlan, self).create(vals)

    # Action Methods
    def action_confirm(self):
        self.write({'state': 'active'})

    def action_complete(self):
        self.write({'state': 'completed'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})



