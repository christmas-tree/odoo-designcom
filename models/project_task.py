# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Task(models.Model):
    _inherit = 'project.task'

    attachment = fields.Binary("Attachment")
    design_sale_order_id = fields.Many2one('sale.order', string="Sale Order")

    def action_take_task(self):
        self.write({
            'user_id': self.env.user.id,
            'stage_id': self.env.ref('sale_design.design_project_stage_1').id,
        })

    def action_submit_for_approval(self):
        if not self.attachment:
            raise UserError(_(
                "There is no attached file to submit."))

        # Send notification
        message = "User %s submitted task %s - %s for approval." % (self.user_id.name, self.name, self.project_id.name)
        manager_group = self.env.ref('sale_design.group_com_manager')
        manager_users = self.env['res.users'].search([('groups_id', '=', manager_group.id)])

        partner_ids = [user.partner_id.id for user in manager_users]

        self.message_post(body=message, subtype='mail.mt_comment', author_id=self.env.user.partner_id.id,
                          partner_ids=partner_ids)

        # update stage
        self.write({
            'stage_id': self.env.ref('sale_design.design_project_stage_2').id,
        })

    def action_approve(self):
        self.design_sale_order_id.attachment = self.attachment
        self.write({
            'stage_id': self.env.ref('sale_design.design_project_stage_3').id,
        })

    def action_reject(self):
        self.write({
            'stage_id': self.env.ref('sale_design.design_project_stage_1').id,
        })
