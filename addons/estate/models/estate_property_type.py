from odoo import models, fields

class EstateModelType(models.Model):
    _name = "estate.property.type"
    _description = "This is type for the main model"

    name = fields.Char(required=True)
    