# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attachment = fields.Binary("Attachment", readonly=True)
    design_task_ids = fields.One2many('project.task', 'design_sale_order_id', string='Associated Tasks')
    design_task_count = fields.Integer(string='Task Count', compute='_compute_task_count', store=False)

    def _compute_task_count(self):
        for order in self:
            order.design_task_count = len(order.design_task_ids)

    def action_confirm(self):
        for order in self:
            if not order.attachment:
                raise UserError(_(
                    "The selected Sales Order should contain an attachment before it can be converted to an invoice."))

        return super(SaleOrder, self).action_confirm()

    def action_view_tasks(self):
        action = self.env.ref('project.action_view_task').read()[0]
        action['view_mode'] = 'tree'
        action['context'] = False
        action['domain'] = [('id', 'in', self.design_task_ids.ids)]
        return action
