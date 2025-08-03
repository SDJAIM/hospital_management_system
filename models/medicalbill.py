from odoo import models, fields, api


class MedicalBill(models.Model):
    _name = 'medical.bill'
    _description = 'Medical Bill'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_name = fields.Char(related='patient_id.name', string='Patient Name', readonly=True)
    patient_age = fields.Char(related='patient_id.age', string='Patient Age', readonly=True)
    patient_gender = fields.Selection(related='patient_id.gender', string='Gender', readonly=True)
    date = fields.Date(string='Date', default=fields.Date.context_today)

    line_ids = fields.One2many('medical.bill.line', 'bill_id', string='Medicine')
    total_amount = fields.Float(string='Total', compute='_compute_total', store=True)

    @api.depends('line_ids.subtotal')
    def _compute_total(self):
        for rec in self:
            rec.total_amount = sum(line.subtotal for line in rec.line_ids)

    def print_medical_bill_report(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': f'/medical/receipt/{self.id}',
            'target': 'new',  # opens the receipt in a new tab
        }

    def action_save_bill_save(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Medical Bills',
            'res_model': 'medical.bill',
            'view_mode': 'list,form',
            'target': 'current',
        }









