# -*- coding: utf-8 -*-
# Copyright 2018 AITIC - Rondón Kristian  <rondonkristian@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class Statistical(models.Model):
    _name = "statistical"

    location_id = fields.Many2one(
        'location',
        'location',
    )
    province_id = fields.Many2one(
        related='location_id.province', store=True,
    )
    censo_home_end = fields.Float('censo final')
    censo_home_start = fields.Float('censo anterior')
    dweller = fields.Integer('quantity dweller')
    competence = fields.Boolean('competence')
    service_present_id = fields.Many2one(
        'service.present',
        string='Place'
    )

class ServicePresent(models.Model):
    _name = "service.present"

    name = fields.Char('name')
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer'
    )
