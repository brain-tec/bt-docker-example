from odoo import api, fields, models

class DummyModel(models.Model):
    _name = 'dummy.model'
    
    name = fields.Char(string='Name', required=True)

