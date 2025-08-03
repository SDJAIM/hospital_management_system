from odoo import models,fields
class MedicineMaster(models.Model):
    _name = 'medicine.master'
    _description = 'Medicine Master'

    name = fields.Char(required=True)
    cost = fields.Float(string='Default Cost')