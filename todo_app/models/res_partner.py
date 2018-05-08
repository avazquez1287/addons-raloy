# -*- coding: utf-8 -*-

from odoo import fields, models

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Tareas personales'

    todo_ids = fields.Many2many('todo.task', string='Equipo de Tareas')


