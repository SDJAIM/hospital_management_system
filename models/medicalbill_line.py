from odoo import models, fields, api

class MedicalBillLine(models.Model):
    _name = 'medical.bill.line'
    _description = 'Medical Bill Line'

    bill_id = fields.Many2one('medical.bill', string='Bill')

    medicine_id = fields.Many2one(
        'medicine.master',
        string='Medicine',
        required=True,
        ondelete='restrict',
        help='Select or create a medicine'
    )

    cost = fields.Float(string='Cost')
    quantity = fields.Integer(string='Quantity', default=1)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('cost', 'quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.cost * line.quantity

    @api.onchange('medicine_id')
    def _onchange_medicine_id(self):
        if self.medicine_id:
            self.cost = self.medicine_id.cost  # Auto-fill cost from master

    @api.onchange('cost')
    def _onchange_cost(self):
        if self.medicine_id and self.cost:
            self.medicine_id.cost = self.cost  # Save cost to master
