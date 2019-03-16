# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

from odoo.addons import decimal_precision as dp
from odoo.tools import float_is_zero

class StockPickingInherited(models.Model):
    # Indicar que debemos a heredar de esta clase
    _inherit = 'stock.picking'

    # Agregamos los campos que necesitamos
    receptor_id = fields.Many2one(
        'res.partner', 'Receptor',
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})