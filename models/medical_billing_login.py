# from odoo import models, fields
# from odoo.exceptions import UserError
#
# class MedicalBillingLogin(models.TransientModel):
#     _name = 'medical.billing.login'
#     _description = 'Medical Billing Login Form'
#
#     email = fields.Char(string='Email', required=True)
#     password = fields.Char(string='Password', required=True)
#
#     def action_redirect_billing(self):
#         if self.email == "med" and self.password == "123":
#             menu = self.env.ref('hospital_management_system.billing', raise_if_not_found=False)
#             if menu:
#                 return {
#                     'type': 'ir.actions.client',
#                     'tag': 'reload',
#                     'params': {'menu_id': menu.id},
#                 }
#             else:
#                 return {'type': 'ir.actions.act_window_close'}
#         else:
#             raise UserError('Invalid credentials!')
