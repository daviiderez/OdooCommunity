from odoo import models, fields, api
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
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[('east', 'East'), ( 'south', 'South'), ('north', 'North'), ('west', 'West')],
        help = "Select an orientation"
    )
    
    partner_id = fields.Many2one('res.users', string="Salesperson",  default=lambda self: self.env.user)
    user_id = fields.Many2one('res.partner', string="Buyer", copy=False)
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', )

    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'), ('offer received', 'Offer Received'), ('offer accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')
        ],
        required=True,
        copy=False,
        default='new'
    )

    # computed fiels
    total_area = fields.Float('Total Area', compute="_compute_total_area")
    best_price = fields.Float('Best Price', compute="_compute_best_price")

    # computed functions
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            try:
                related_values = max(record.offer_ids.mapped('price'))
            except:
                related_values = 0
            record.best_price = related_values 
    
    @api.onchange("garden")
    def _onchange_garden(self):
        _val = self.garden == True
        self.garden_area = 10 if _val else 0
        self.garden_orientation = "north" if _val else 0
        
