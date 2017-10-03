# -*- coding: utf-8 -*-

from odoo import models, fields, api

class i4s_survey_suggest(models.Model):
    _name = 'i4s.survey.suggest'
    
    _rec_name = 'survey_question_code'
    
    survey_question_id = fields.Text(string='ID câu hỏi')
    survey_question_code = fields.Text(string='Mã câu hỏi')
    current = fields.Text(string='Điểm hiện tại')
    advisor = fields.Text(string='Cố vấn')
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