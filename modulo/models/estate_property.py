from odoo import fields, models

class TestModel(models.Model):
    _name = "estate.property"
    _description = "Test Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char('postcode')
    date_availability = fields.Datetime('date_availability', default=fields.Datetime.now)
    expected_price = fields.Float('expected_price', required=True)
    selling_price= fields.Float('selling_price', readonly=True)
    bedrooms = fields.Integer('bedrooms',default='2')
    living_area = fields.Integer('living_area')
    facades = fields.Integer('facades')
    garage = fields.Boolean('garage')
    garden = fields.Boolean('garden')
    garden_area = fields.Integer('garden_area')
    garden_orientation = lead_type = fields.Selection([('North','North'),('South','South'),('East','East'),('West','West')])