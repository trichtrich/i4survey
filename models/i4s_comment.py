# -*- coding: utf-8 -*-

from odoo import models, fields, api

class i4s_comment(models.Model):
    _name = 'i4s.comment'
    
    data_item_id = fields.Integer(string='Mã danh mục')
    c_00_05 = fields.Char(string='0 -> 0.5')
    c_05_10 = fields.Char(string='0.5 -> 1')
    c_10_15 = fields.Char(string='1 -> 1.5')
    c_15_20 = fields.Char(string='1.5 -> 2')
    c_20_25 = fields.Char(string='2 -> 2.5')
    c_25_30 = fields.Char(string='2.5 -> 3')
    c_30_35 = fields.Char(string='3 -> 3.5')
    c_35_40 = fields.Char(string='3.5 -> 4')
    c_40_45 = fields.Char(string='4 -> 4.5')
    c_45_50 = fields.Char(string='4.5 -> 5')
