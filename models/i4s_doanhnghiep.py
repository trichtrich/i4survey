# -*- coding: utf-8 -*-

from odoo import models, fields, api

class i4s_doanhnghiep(models.Model):
    _name = 'i4s.doanhnghiep'
    
    _rec_name = 'ten_doanhnghiep'
    
    ten_doanhnghiep = fields.Text(string='Tên doanh nghiệp')
    ten_doanhnghiep_en = fields.Text(string='Tên doanh nghiệp (EN)')
    diachi = fields.Text(string='Địa chỉ')
    sodienthoai = fields.Text(string='Số điện thoại')
    so_gpkd = fields.Text(string='Số giấy phép kinh doanh')
    nguoi_daidien = fields.Text(string='Người đại diện')
    fax = fields.Text(string='Fax')
    email = fields.Text(string='Email')
    maso_thue = fields.Text(string='Mã số thuế')
    linhvucid = fields.Integer(string='Lĩnh vực')
    loaihinhid = fields.Integer(string='Loại hình')
    result = fields.Text(string='Kết quả')
    is_send = fields.Integer(string='Đã gửi')
    chien_luoc = fields.Text(string='Chiến lược')
    lanh_dao = fields.Text(string='Lãnh đạo')
    san_pham = fields.Text(string='Sản phẩm')
    khach_hang = fields.Text(string='Khách hàng')
    van_hanh = fields.Text(string='Vận hành')
    van_hoa = fields.Text(string='Văn hóa')
    con_nguoi = fields.Text(string='Con người')
    chinh_sach = fields.Text(string='Chính sách')
    cong_nghe = fields.Text(string='Công nghệ')
    sonhanvien = fields.Integer(string='Số nhân viên')
    doanhthu = fields.Text(string='Doanh thu')
# class i4survey(models.Model):
#     _name = 'i4survey.i4survey'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100