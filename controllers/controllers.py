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
		lv1_list = http.request.env['i4s.data.item'].sudo().search([('datagroupid', '=', 1), ('level', '=', 1)], order='displayorder asc')
		for lv1 in lv1_list:
			r = {}
			r['name'] = lv1.name
			r['image'] = lv1.display_image

			groups = []
			lv2_list = http.request.env['i4s.data.item'].sudo().search([('datagroupid', '=', 1), ('node_1', '=', lv1.node_1), ('level', '=', 2)])
			
			for lv2 in lv2_list:
				g = {}
				g['display'] = lv2.display
				g['name'] = lv2.name
				g['description'] = lv2.description

				lv3_list = http.request.env['i4s.data.item'].sudo().search([('datagroupid', '=', 1), ('node_2', '=', lv2.node_2), ('level', '=', 3)])
				g['questions'] = lv3_list

				groups.append(g)

			r['groups'] = groups

			results.append(r)

		return http.request.render('i4survey.i4s_homepage', {
			'results': results
		})

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
