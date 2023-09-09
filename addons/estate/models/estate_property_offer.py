from odoo import _, api, fields, models
from dateutil.relativedelta import relativedelta
from math import ceil

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer Description'
    
    price = fields.Float('Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status')

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date().add(fields.Date.today(),days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            _pre = (record.date_deadline - record.create_date.date()).days
            record.validity = _pre
    