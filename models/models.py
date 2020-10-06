# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    attachment = fields.Binary("Attachment")


class Task(models.Model):
    _inherit = 'project.task'

    attachment = fields.Binary("Attachment")


class ProjectCreateInvoice(models.TransientModel):
    _inherit = 'project.create.invoice'

    def action_create_invoice(self):
        if not self.attachment:
            raise UserError(_("The selected Sales Order should contain an attachment before it can be converted to an invoice."))

        return super(ProjectCreateInvoice, self).action_create_invoice()
