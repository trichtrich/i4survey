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

		return http.request.render('i4survey.i4s_home')


class i4survey(http.Controller):
	@http.route('/survey', auth='public', methods=['POST'], website=True)
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
			
			x_result = http.request.env['i4s.data.item'].sudo().search([('datagroupid', '=', 1), ('level', '=', 3)])
			for i in x_result:

				answer = kw.get('answer_' + str(i.id))
				expected = i.trong_so * float(answer) / 100
				http.request.env['i4s.survey.result'].sudo().create({
					'survey_question_id': str(i.id),
					'survey_question_code': i.node_2,
					'doanhnghiepid': str(doanhnghiep.id),
					'current': answer,
					'expected': expected
				})

			http.request.env['crm.lead'].sudo().create({
				'name' : ten_doanhnghiep,
				'partner_name' : ten_doanhnghiep,
				'email_from' : email,
				'street' : diachi,
				'phone' : sodienthoai,
				'contact_name' : nguoi_daidien
			})

			#lv2_list = http.request.env['i4s.data.item'].sudo().search([('datagroupid', '=', 1), ('node_1', '=', lv1.node_1), ('level', '=', 2)])

		#template = http.request.env.ref('i4survey.doanhnghiep_mail_template')
		#http.request.env['mail.template'].sudo().browse(template.id).send_mail(doanhnghiep.id, force_send=True)
		return http.request.render('i4survey.i4survey_thank_you')



	@http.route('/i4survey/results/<int:doanhnghiepid>', type='http', auth="public", website=True)
	def view_result(self, doanhnghiepid, **kw):

		doanhnghiep = http.request.env['i4s.doanhnghiep'].sudo().browse([doanhnghiepid])

		results = []
		tabval = []
		total_all = 0
		lv1_list = http.request.env['i4s.data.item'].sudo().search([('datagroupid', '=', 1), ('level', '=', 1)], order='displayorder asc')
		for lv1 in lv1_list:
			r = {}
			r['idstr'] = lv1.id
			r['name'] = lv1.name
			r['image'] = lv1.display_image


			groups = []
			lv2_list = http.request.env['i4s.data.item'].sudo().search([('datagroupid', '=', 1), ('node_1', '=', lv1.node_1), ('level', '=', 2)])
			
			for lv2 in lv2_list:
				
				total = 0
				i4survey_results = http.request.env['i4s.survey.result'].sudo().search([('survey_question_code', '=', lv2.code), ('doanhnghiepid', '=', str(doanhnghiep.id))])
				for t in i4survey_results:
					total += float(t.expected)
				
				total_all += total
				g = {}
				g['display'] = lv2.display
				g['name'] = lv2.name
				g['total'] = total
				groups.append(g)

			r['groups'] = groups

			
			ta = {}
			ta['name'] = lv1.name
			total_all = total_all / len(lv2_list)
			#_logger.info('-------------total_all---------------: ' + str(round(total_all,2)))
			ta['total_all'] = round(total_all,2)
			tabval.append(ta)

			results.append(r)
		data = {
			'results': results,
			'resultsTab1': tabval
		}

		return http.request.render('i4survey.i4s_result', data)


	@http.route('/i4survey', type='http', auth="public", website=True)
	def i4survey(self, **kw):
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
