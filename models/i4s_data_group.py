# -*- coding: utf-8 -*-

from odoo import models, fields, api

class i4s_data_group(models.Model):
    _name = 'i4s.data.group'
    
    _rec_name = 'name'
    
    code = fields.Text(string='Mã')
    name = fields.Text(string='Tên')
    description = fields.Text(string='Mô tả')
    
# class i4survey(models.Model):
#     _name = 'i4survey.i4survey'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100