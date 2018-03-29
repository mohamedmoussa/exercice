# -*- coding: utf-8 -*-
from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    exercice = fields.Char(string="Task")
    page_id = fields.Many2one(comodel_name="task.page", string="Page", required=False, )
