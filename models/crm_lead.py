
from odoo import http
from odoo import models, fields, api, _
from odoo.http import request
from odoo.addons.base.res.res_partner import FormatAddress

class Lead(FormatAddress, models.Model):
	_inherit = "crm.lead"


	result_url = fields.Char(string='Result URL')
	status_mail = fields.Selection([('draft', 'Draft'), ('success', 'Success')], string='Status Result', default='draft')


	@api.multi
	def action_send_mail(self):
		for record in self:

			record.status_mail = 'success'

			template = http.request.env.ref('i4survey.doanhnghiep_mail_template')
			self.env['mail.template'].sudo().browse(template.id).send_mail(record.id, force_send=True)