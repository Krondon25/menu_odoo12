# -*- coding: utf-8 -*-
# Copyright 2018 AITIC - Rondón Kristian  <rondonkristian@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class Location(models.Model):
    _name = "location"

    name = fields.Char(string='Location', required=True,)
    province = fields.Many2one('res.country')
    ubication = fields.Char(string='address google maps')
