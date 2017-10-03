# -*- coding: utf-8 -*-

from odoo import models, fields, api

class i4SDaTaItem(models.Model):
	_name = 'i4s.data.item'

	datagroupid = fields.Integer('datagroupid', track_visibility='always')
	code = fields.Char(string='CODE')
	node_1 = fields.Char(string='NODE_1')
	node_2 = fields.Char(string='NODE_2')
	node_3 = fields.Char(string='NODE_3')
	node_4 = fields.Char(string='NODE_4')
	level = fields.Integer()
	name = fields.Text(string='name')
	description = fields.Text(string='Mô tả')
	display = fields.Char(string='Hiển thị')
	status = fields.Integer(string='Trạng thái')
	displayorder = fields.Integer(string='displayorder')
	validatefrom = fields.Datetime(string='VALIDATEDFROM', readonly=True)
	validateto = fields.Datetime(string='VALIDATEDTO', readonly=True)
	result = fields.Char(string='result')
	isSend = fields.Integer(string='isSend')