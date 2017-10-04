# -*- coding: utf-8 -*-
import logging

from odoo import http, _
from odoo.addons.website.controllers.main import Website

_logger = logging.getLogger(__name__)

class Website(Website):
	@http.route(auth='public')
	def index(self, data={}, **kw):
		super(Website, self).index(**kw)
		return http.request.render('i4survey.i4s_homepage', data)

class Home(http.Controller):

	@http.route('/survey', auth='public')
	def survey(self, **kw):

		chienluocs = search_dataitem('i4s.data.item', 1, '01', 2)
		lanhdaos  = search_dataitem('i4s.data.item', 1, '02', 2)
		sanphams  = search_dataitem('i4s.data.item', 1, '03', 2)
		khachhanngs  = search_dataitem('i4s.data.item', 1, '04', 2)
		vanhanhs  = search_dataitem('i4s.data.item', 1, '05', 2)
		vanhoas  = search_dataitem('i4s.data.item', 1, '06', 2)
		connguois  = search_dataitem('i4s.data.item', 1, '07', 2)
		chinhsachs  = search_dataitem('i4s.data.item', 1, '08', 2)
		congnghes  = search_dataitem('i4s.data.item', 1, '09', 2)

		linhvucs = search_dataitem('i4s.data.item', 2, '', 1)


		data = {
			'chienluocs': chienluocs,
			'lanhdaos': lanhdaos,
			'sanphams': sanphams,
			'khachhanngs': khachhanngs,
			'vanhanhs': vanhanhs,
			'vanhoas': vanhoas,
			'connguois': connguois,
			'chinhsachs': chinhsachs,
			'congnghes': congnghes,
			'linhvucs': linhvucs
		}

		return http.request.render('i4survey.homepage', data)



	def search_dataitem(table, datagroupid, code, level):

		domain = []

		if datagroupid > 0:
			domain += [('datagroupid', '=', datagroupid)]

		if code != '':
			domain += [('code', '=', code)]

		if level > 0:
			domain =+ [('level', '=', level)]

		results = http.request.env[table].sudo().search(domain)
		return results