# -*- coding: utf-8 -*-


from odoo import fields, models

class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'Etiqueta de Tarea'
    _parent_store = True

    name = fields.Char('Name', translate=True)
    taks_ids = fields.Many2many('todo.task', string='Tareas')
    parent_id = fields.Many2one('todo.task.tag', 'Etiqueta Padre', ondelete='restrict')
    parent_left = fields.Integer('Parent Left', index=True)
    parent_right = fields.Integer('Parent Right', index=True)