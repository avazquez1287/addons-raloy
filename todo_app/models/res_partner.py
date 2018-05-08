# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    todo_ids = fields.Many2many('todo.task', string='Equipo de Tareas')


