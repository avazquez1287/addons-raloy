# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exception import ValidationError
import logging
#el name se refiere a esta instancia
_logger = logging.getLogger(__name__)


class TodoTaskWizard(models.TransientModel):
    _name = 'todo.task.wizard'
    _decription = 'Asignacion masiva de Tareas'

    task_ids = fields.Many2many('todo.task', string='Tareas')  #Indispensable usar Many2many
    new_deadline = _fields.Date('Nueva Fecha Limite')
    new_user_id = fields.Many2many('res.user', string='Nuevo responsable')

    @api.multi
    def do_reopend_wizard(self):
        self.ensure_one()
        return  {
            'type': 'ir.action.act_window',
            'res_model': self._name, # Nombre del modelo
            'res_id': self.id, #identificador actual del registro del wizard
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new'
        }


    @api.multi
    def do_load_tasks(self):
        self.ensure_one()
        task = self.env['todo.task']
        tasks = task.search([])
        self.task_ids = tasks
        _logger.info('Se cargaron  %d' % len(tasks))
        return self.do_reopend_wizard

    @api.multi
    def do_count_tasks(self):
        task = self.env['todo.task']
        count = task.search_count([])
        #opciones para dar formato
        raise ValidationError('Existen %d tareas activas' %count)
        #raise ValidationError('Existen {} tareas activas' .format(count)

    @api.multi
    def do_mass_update(self):
        self.ensure_one()#restringe para un solo elemento del recordset

        if not(self.new_deadline or self.new_user_id or self.task_ids):
            raise ValidationError('No har datos para actualizar')

        #Diccionario

        valores = {}
        if self.new_user_id:
            _logger.info('Nuevo Usuario {}', format(self.new_user_id))
            valores.update({'user_id': self.new_user_id.id})
        if self.new_deadline:
            _logger.info('Nueva fecha limite {}', format(self.new_deadline))
            valores.update({'date_deadline': self.new_deadline})

        self.task_ids.write(valores)
        return True






