# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    #constrain basado en sql para validar que no se repirtan los
    #Estructura
    #  _sql_constrains = [('nombre','funcion de posgres', 'Mensaje')]
    _sql_constrains = [('todo_task_name_unique','UNIQUE(name, user_id, active)',
                        'Ya existe una tarea con el mismo nombre')]


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
    user_todo_count = fields.Integer('Tareas asignada', compute='_compute_user_todo_count', store=True)
    stage_fold = fields.Boolean(string='Etapa Doblada',
                                compute='_compute_stage_fold',
                                search='search_Stage_fold',
                                inverse='_werite_stage_fold'
                                )




    #Se indica que queremos los dos modelos en la referencia
    refers_to = fields.Reference([('res.user', 'User'), ('res.partner', 'Partner')], 'Referncia')

    # Constrain basado en python
    @api.multi
    @api.constrains('name')
    def check_name_size(self):
        for task in self:
            if len(task.name) > 50 or len(task.name) < 5:
                raise ValidationError('Minimo 5 y maximo 50 caracteres')



    @api.model #cuando se utiliza la api model no recibe un recordset
    def creat(self,vals):
        values.update({'effort_estimate':5})
        new_record = super(TodoTask, self).creat(values) #Para modulos en odoo 10 se usa esta sentencia
        return new_record


    @api.multi#la api multi se utliza para borrar o modificar un registro existente
    @api.onchange('user_id')#lanzar un evento cada vez que cambie l user_id
    def onchange_user_id(self):
        if not self.user_id:
            self.team_ids = None
            return {
                'warning': {
                    'title': 'Sin usuario responsable',
                    'message': 'Se vacacionaron los miembros del equipo'
                }
            }

    @api.multi
    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold

    @api.multi
    def _serch_satage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    @api.multi
    def _write_stage_fold(self, operator, value):
        self.stage_id.fold = self.stage_fold


    @api.multi
    @api.depends('user_id')
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
