# -*- coding: utf-8 -*-
# Copyright 2018 AITIC - Rondón Kristian  <rondonkristian@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    service_present_id = fields.One2many('service.present', 'customer_id', string='Service Present')
    