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
		counttitle = self.search_dataitem('i4s.data.item', 1, '', 1)

		for x in counttitle:
			x_result = self.search_dataitem('i4s.data.item', 1, x.node_1, 2)
			name = x.name
			image = x.display_image
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






	def search_dataitem(self, table, datagroupid, node_1, level):

		domain = []

		if datagroupid > 0:
			domain.append(('datagroupid', '=', datagroupid))

		if node_1 != '':
			domain.append(('node_1', '=', node_1))

		if level > 0:
			domain.append(('level', '=', level))

		results = http.request.env[table].sudo().search(domain)
		return results



	@http.route('/survey', auth='public')
	def create_survey(self, **kw):
		nguoi_daidien = kw.get('nguoi_daidien')
		sodienthoai = kw.get('sodienthoai')
		email = kw.get('email')
		ten_doanhnghiep = kw.get('ten_doanhnghiep')
		linhvucid = kw.get('linhvucid')
		sonhanvien = kw.get('sonhanvien')
		doanhthu = kw.get('doanhthu')
		diachi = kw.get('diachi')



		doanhnghiep = http.request.env['i4s.doanhnghiep'].sudo().create({
			'nguoi_daidien': nguoi_daidien,
			'sodienthoai': sodienthoai,
			'email': email,
			'ten_doanhnghiep': ten_doanhnghiep,
			'linhvucid': linhvucid,
			'sonhanvien': sonhanvien,
			'doanhthu': doanhthu,
			'diachi': diachi
		})
		if doanhnghiep:
			counttitle = self.search_dataitem('i4s.data.item', 1, '', 1)

			for x in counttitle:
				x_result = self.search_dataitem('i4s.data.item', 1, x.node_1, 2)
				for i in x_result:

					answer = kw.get('answer_' + str(i.id))

					http.request.env['i4s.survey.result'].sudo().create({
						'survey_question_id': str(i.id),
						'survey_question_code': i.code,
						'doanhnghiepid': str(doanhnghiep.id),
						'current': answer
					})


		return http.request.render('i4survey.i4s_homepage', {
            'message': 'Khảo sát thành công'
        })
