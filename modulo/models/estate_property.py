from odoo import fields, models

class TestModel(models.Model):
    _name = "estate_property"
    _description = "Test Model"

    name = fields.Char()
    description = fields.Text()
