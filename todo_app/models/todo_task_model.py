# -*- coding: utf-8 -*-

from odoo import fields, models

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Tareas personales'

    name = fields.Char('Descripcion', required=True)
    is_done = fields.Boolean('Terminado?')
    active = fields.Boolean('Activa ?', default=True)
    user_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Equipo')

