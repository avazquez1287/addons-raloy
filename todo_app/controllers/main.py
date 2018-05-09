# -*- coding: utf-8 -*-

from odoo import http

class Todo(http.Controller):

    @http.route('/tareas', auth='public')
    def Main(self, **kwargs):
        TodoTask = http.request.env['todo.task']
        tasks = TodoTask.search([('is_done', '=', False)])
        return http.request.render('todo_app.index_template', {'tasks': tasks})
