# -*- coding: utf-8 -*-
from odoo import http

# class I4survey(http.Controller):
#     @http.route('/i4survey/i4survey/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/i4survey/i4survey/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('i4survey.listing', {
#             'root': '/i4survey/i4survey',
#             'objects': http.request.env['i4survey.i4survey'].search([]),
#         })

#     @http.route('/i4survey/i4survey/objects/<model("i4survey.i4survey"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('i4survey.object', {
#             'object': obj
#         })