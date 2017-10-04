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
			x_result = self.search_dataitem('i4s.data.item', 1, '0'+str(i), 1)
			names = self.search_dataitem('i4s.data.item', 1, '0'+str(i), i)
			name = names[0].name
			image = names[0].display_image
			e  = {}
			e['name'] = name
			e['image'] = image
			e['questions'] = x_result

			results.append(e)


		linhvucs = self.search_dataitem('i4s.data.item', 2, '', 1)

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



	def search_dataitem(self, table, datagroupid, code, level):

		domain = []

		if datagroupid > 0:
			domain.append(('datagroupid', '=', datagroupid))

		if code != '':
			domain.append(('code', '=', code))

		if level > 0:
			domain.append(('level', '=', level))

		results = http.request.env[table].sudo().search(domain)
		return results