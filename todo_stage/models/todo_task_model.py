# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    effort_estimate = fields.Integer()
    name = fields.Char(help=u'¿Qué es lo que se tiene que hacer?')

    stage_id = fields.Many2one('todo.task.stage', 'Etapa')
    tag_ids = fields.Many2many(
        comodel_name='todo.task.tag',   # modelo relacionado o co_modelo
        relation='todo_task_tag_rel',   # nombre de la tabla relacion
        column1='task_id',              # nombre de la columna que referencia a todo.task
        column2='tag_id',               # nombre de la columna que referencia a todo.task.tag
        string='Etiquetas',             # etiqueta (string)
        )

    partner_id = fields.Many2one('res.partner', string='Contacto', related='user_id.partner_id', readonly=True)
    state = fields.Selection(related='stage_id.state', string='Estatus de la Etapa')

    # campo calculado
    user_todo_count = fields.Integer('Tareas asignada', compute='_compute_user_todo_count')


    @api.multi
    def _compute_user_todo_count(self):
        for task in self:
            task.user_todo_count = task.search_count([('user_id', '=', task.user_id.id)])

    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
        #  Tarea_terminada == True AND ( Usuario == uid OR Usuario == False )
        dones = self.search(domain)
        dones.write({'active': False})

        return True

    @api.multi
    def do_toggle_done(self):
        for task in self:

            print(task.user_id.name)

            if task.user_id != self.env.user:
                raise ValidationError('Solo el usuario responsable puede hacer esto')

            task.is_done = not task.is_done
        return True
