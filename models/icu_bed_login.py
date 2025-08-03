# from odoo import models, fields
# from odoo.exceptions import UserError
#
# class ICUBedLogin(models.TransientModel):
#     _name = 'icu.bed.login'
#     _description = 'ICU Bed Login Form'
#
#     email = fields.Char(string='Email', required=True)
#     password = fields.Char(string='Password', required=True)
#
#     def action_redirect_icu(self):
#         if self.email == "icu" and self.password == "123":
#             menu = self.env.ref('hospital_management_system.menu_icu_booking', raise_if_not_found=False)
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
