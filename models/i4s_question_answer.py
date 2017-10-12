# -*- coding: utf-8 -*-

from odoo import models, fields, api

class question_answer(models.Model):
	_name = 'i4s.question.answer'


	question_id = fields.Many2one('i4s.data.item')
	answer_content = fields.Text('Answer content')
	answer_value = fields.Text('Answer value')