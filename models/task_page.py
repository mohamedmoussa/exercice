# -*- coding: utf-8 -*-
from openerp import models, fields, api


class TaskPage(models.Model):
    _name = 'task.page'

    name = fields.Char(string="Number Page")
