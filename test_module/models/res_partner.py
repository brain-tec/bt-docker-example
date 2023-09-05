##############################################################################
# Copyright (c) 2021 brain-tec AG (https://bt-group.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################


from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    demo_field = fields.Char()
