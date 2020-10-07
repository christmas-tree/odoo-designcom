# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Task(models.Model):
    _inherit = 'project.task'

    attachment = fields.Binary("Attachment")
    design_sale_order_id = fields.Many2one('sale.order', string="Associated Sale Order")
