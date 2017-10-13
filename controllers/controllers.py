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
		module_name = 'Đánh giá DN du lịch'



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

			base_url = http.request.env['ir.config_parameter'].get_param('web.base.url')
			result_url = ''

			link_tracker = http.request.env['link.tracker'].sudo().create({
				'title' : module_name,
				'url' : base_url + '/i4survey/results/' + str(doanhnghiep.id),
				'medium_id' : 4,
				'source_id' : 6
			})

			if link_tracker:
				result_url = link_tracker.short_url

			http.request.env['crm.lead'].sudo().create({
				'name' : module_name,
				'partner_name' : ten_doanhnghiep,
				'email_from' : email,
				'street' : diachi,
				'phone' : sodienthoai,
				'contact_name' : nguoi_daidien,
				'result_url' : result_url,
				'status_mail' : 'draft'
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
		tab1_total_all = 0
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

			total_all = total_all / len(lv2_list)
			total_all = round(total_all, 2)
			tab1_total_all += total_all
			r['total_all'] = total_all
			comment = ''
			comments = http.request.env['i4s.comment'].sudo().search([('data_item_id', '=', lv1.id)])
			if comments:
				if total_all > 0 and total_all <= 0.5:
					comment = comments['c_00_05']
				elif total_all > 0.5 and total_all <= 1:
					comment = comments['c_05_10']
				elif total_all > 1 and total_all <= 1.5:
					comment = comments['c_10_15']
				elif total_all > 1.5 and total_all <= 2:
					comment = comments['c_15_20']
				elif total_all > 2 and total_all <= 2.5:
					comment = comments['c_20_25']
				elif total_all > 2.5 and total_all <= 3:
					comment = comments['c_25_30']
				elif total_all > 3 and total_all <= 3.5:
					comment = comments['c_30_35']
				elif total_all > 3.5 and total_all <= 4:
					comment = comments['c_35_40']
				elif total_all > 4 and total_all <= 4.5:
					comment = comments['c_40_45']
				elif total_all > 4.5 and total_all <= 5:
					comment = comments['c_45_50']
			r['comment'] = comment

			ta = {}
			ta['name'] = lv1.name
			#_logger.info('-------------total_all---------------: ' + str(round(total_all,2)))
			ta['total_all'] = total_all
			tabval.append(ta)

			results.append(r)

		tab1_total_all = tab1_total_all / len(lv1_list)
		tab1_total_all = round(tab1_total_all, 2)
		tab1_comment = ''
		tab1_comments = http.request.env['i4s.comment'].sudo().search([('data_item_id', '=', 0)])
		if tab1_comments:
			if tab1_total_all == 0:
				tab1_comment = tab1_comments['c_00']
			if tab1_total_all > 0 and tab1_total_all <= 0.5:
				tab1_comment = tab1_comments['c_00_05']
			elif tab1_total_all > 0.5 and tab1_total_all <= 1:
				tab1_comment = tab1_comments['c_05_10']
			elif tab1_total_all > 1 and tab1_total_all <= 1.5:
				tab1_comment = tab1_comments['c_10_15']
			elif tab1_total_all > 1.5 and tab1_total_all <= 2:
				tab1_comment = tab1_comments['c_15_20']
			elif tab1_total_all > 2 and tab1_total_all <= 2.5:
				tab1_comment = tab1_comments['c_20_25']
			elif tab1_total_all > 2.5 and tab1_total_all <= 3:
				tab1_comment = tab1_comments['c_25_30']
			elif tab1_total_all > 3 and tab1_total_all <= 3.5:
				tab1_comment = tab1_comments['c_30_35']
			elif tab1_total_all > 3.5 and tab1_total_all <= 4:
				tab1_comment = tab1_comments['c_35_40']
			elif tab1_total_all > 4 and tab1_total_all <= 4.5:
				tab1_comment = tab1_comments['c_40_45']
			elif tab1_total_all > 4.5 and tab1_total_all <= 5:
				tab1_comment = tab1_comments['c_45_50']

		data = {
			'results': results,
			'resultsTab1': tabval,
			'tab1_comment': tab1_comment
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
				questions = []

				for a in lv3_list:
					list_answers = http.request.env['i4s.question.answer'].sudo().search([('question_id', '=', a.id)])
					q = {
						'id': a.id,
						'name': a.name,
						'list_answers': list_answers
					}
					questions.append(q)

				g['questions'] = questions

				groups.append(g)

			r['groups'] = groups

			results.append(r)

		return http.request.render('i4survey.i4s_homepage', {
			'results': results
		})
