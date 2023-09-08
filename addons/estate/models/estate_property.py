from odoo import models, fields
from dateutil.relativedelta import relativedelta

class EstateModel(models.Model):
    _name = "estate.property"
    _description = "This is a model for register properties"

    name = fields.Char(required=True)
    property_type = fields.Many2one("estate.property.type", string="Property Type")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.today() + relativedelta(months=+3) )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2, copy=False)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Boolean()
    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[('east', 'East'), ( 'south', 'South'), ('north', 'North'), ('west', 'West')],
        help = "Select an orientation"
    )
    
    partner_id = fields.Many2one('res.users', string="Salesperson",  default=lambda self: self.env.user)
    user_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tags")

    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')
        ],
        required=True,
        copy=False,
        default='new'
    )