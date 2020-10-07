from odoo import fields, models, api, _
from odoo.exceptions import UserError


class CreateTask(models.TransientModel):
    _name = 'sale_design.create_task'
    _description = 'Transient model to create new design task'

    name = fields.Char(string='Title', trequired=True)
    type = fields.Selection(string='Design type', required=True,
                            selection=[
                                ('2d', '2D Design'),
                                ('3d', '3D Design'),
                            ])
    user_id = fields.Many2one('res.users', string='Assigned to', required=True)
    date_deadline = fields.Date(string='Deadline', required=True)

    def action_create_task(self):
        project = 'sale_design.design_2d_project' if self.type == '2d' else 'sale_design.design_3d_project'

        active_order_id = self._context.get('active_id', False)
        self.env['project.task'].create({
            'name': self.name,
            'project_id': self.env.ref(project).id,
            'user_id': self.user_id.id,
            'date_deadline': self.date_deadline,
            'design_sale_order_id': active_order_id,
        })
