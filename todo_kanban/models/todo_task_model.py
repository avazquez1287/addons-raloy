# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
   # _name = 'todo.task'
    _inherit = 'todo.task'

    color = fields.Integer('Color')
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Normal'),
        ('2', 'Alta'),
    ], 'Prioridad', default='1')
    kanban_state = fields.Selection([
        ('normal', 'En Progreso'),
        ('blocked', 'Bloqueado'),
        ('done', 'Lista para la etapa siguiente'),
    ], 'Estado Kanban', default='normal')