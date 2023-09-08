from odoo import _, api, fields, models

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag Description'
    
    name = fields.Char('Tag Name')