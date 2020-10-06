# -*- coding: utf-8 -*-
# from odoo import http


# class SaleDesign(http.Controller):
#     @http.route('/sale_design/sale_design/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_design/sale_design/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_design.listing', {
#             'root': '/sale_design/sale_design',
#             'objects': http.request.env['sale_design.sale_design'].search([]),
#         })

#     @http.route('/sale_design/sale_design/objects/<model("sale_design.sale_design"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_design.object', {
#             'object': obj
#         })
