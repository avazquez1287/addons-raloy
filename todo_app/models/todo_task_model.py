# -*- coding: utf-8 -*-

from odoo import fields, models, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Tareas personales'

    name = fields.Char('Descripcion', required=True)
    is_done = fields.Boolean('Terminado?')
    active = fields.Boolean('Activa ?', default=True)
    user_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Equipo')
    date_deadline = fields.Date('Fecha Limite', required=True)

    @api.multi
    def do_clear_done(self):
     #self representa un recordset
         for task in self:
              if task.is_done:
                  task.active = False
         return True

    @api.multi
    def write(self, values):
         if 'active' not in values:
             values ['active'] = True

         super(TodoTask, self).write(values)