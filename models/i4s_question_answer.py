# -*- coding: utf-8 -*-

from odoo import models, fields, api

class question_answer(models.Model):
	_name = 'i4s.question.answer'


	question_id = fields.Many2one('i4s.data.item')
	question_answer = fields.Text('Answer')