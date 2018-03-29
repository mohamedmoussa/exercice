# -*- coding: utf-8 -*-
from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    exercice = fields.Char('Task')

 