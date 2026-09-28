from odoo import api, models, fields


class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real estate Model"

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    state = fields.Selection(
            [
                ("new", "New"),
                ("received", "Offer Received"),
                ("accepted", "Offer Accepted"),
                ("sold", "Sold"),
                ("canceled","Canceled"),
                ],
            required=True,
            copy=False,
            default="new"
            )

    postcode = fields.Char()
    
    def default_date(self):
        return fields.Date.today()

    date_availability = fields.Date(default= default_date)
    expected_price = fields.Float(required=True)
    best_offer = fields.Float()
    selling_price = fields.Float()
    
    description = fields.Text()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
    ])

    property_type_id = fields.Many2one(
            "estate.property.type",
            string="Property Type",
            )

    buyer_id = fields.Many2one(
            "res.partner",
            string="Buyer",
            copy=False,
            )

    salesperson_id = fields.Many2one(
            "res.users",
            string="Salesperson",
            default=lambda self: self.env.user,
            )

    offer_ids = fields.One2many(
            "estate.property.offer",
            "property_id",
            string="Offers",
            )

    tag_ids = fields.Many2many("estate.property.tag")

    total_area = fields.Float(compute="_compute_total_area")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area


    best_price = fields.Float(compute="_compute_best_price")

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for rec in self:
            rec.best_price = max(rec.offer_ids.mapped("price"), default=0.0)

    @api.onchange("garden")
    def _onchange_garden(self):
        for estate in self:
            if not estate.garden:
                estate.garden_area = 0

            
