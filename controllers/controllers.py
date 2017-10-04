# -*- coding: utf-8 -*-
import logging
import re
import unicodedata

from odoo import http, _
from odoo.addons.website.controllers.main import Website

_logger = logging.getLogger(__name__)

class Website(Website):
	@http.route(auth='public')
	def index(self, data={}, **kw):
		super(Website, self).index(**kw)

		results = []

		for i in range(1, 10):
...     	print('0'+str(i))
			x_result = search_dataitem('i4s.data.item', 1, '0'+str(i), 2)
			names = search_dataitem('i4s.data.item', 1, '0'+str(i), i)
			name = names[0].name
			e  = {}
			e['name'] = name
			e['questions'] = x_result

			results.append(e)


		linhvucs = search_dataitem('i4s.data.item', 2, '', 1)

		data = {
			'results': results,
			'linhvucs': linhvucs
		}

		return http.request.render('i4survey.i4s_homepage', data)



	def no_ac_vi(s):
		s = s.decode('utf-8')
		s = re.sub(u'Đ', 'D', s)
		s = re.sub(u'đ', 'd', s)
		return unicodedata.normalize('NFKD', unicode(s)).encode('ASCII', 'ignore')



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