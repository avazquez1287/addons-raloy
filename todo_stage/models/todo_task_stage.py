# -*- coding: utf-8 -*-


from odoo import fields, models

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'Etapas de Tareas'
    _order = 'sequence,name'

    name = fields.Char('Name', translate=True)
    desc = fields.Text('Description')
    state = fields.Selection(string='Estado', selection=[('draft', 'Nuevo'),('open', 'Iniciado'), ('done', 'Cerrado')])
    docs = fields.Html(u'Documentación')  # String en formato UNICODE

    # Campos numericos
    perc_complete = fields.Float('% Terminado', (3, 2))
    sequence = fields.Integer('Sequence')

    # Campos de fecha
    date_effective = fields.Date('Fecha Efectiva')
    date_created = fields.Datetime(u'Fecha y hora de creación', default=lambda self: fields.Datetime.now())

    fold = fields.Boolean('Doblada?')
    image = fields.Binary('Imagen')

    # Relacion con Tareas
    task_ids = fields.One2many(
        'todo.task',        # modelo relacionado
        'stage_id',         # campo relacionado con el modelo
        'Tareas en esta etapa'
    )