# -*- coding: utf-8 -*-

from odoo import fields, models, api


class TodoTask(models.Model):
    _inherit = 'todo.task'

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
