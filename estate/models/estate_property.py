from odoo import models, fields, api
from datetime import timedelta, date  # Import timedelta and date for default values

class EstateProperty(models.Model):
    _name = "estate.property"  # Model name (used for database storage)
    _description = "Real Estate Property"  # Description of the model

    # Basic Property Information
    name = fields.Char(
        string="Title",
        required=True,
    )

    description = fields.Text(string="Description")

    postcode = fields.Char(string="Postcode")

    available_from = fields.Date(
        string="Available From",
        copy=False,
        default=lambda self: date.today() + timedelta(days=90),
    )

    expected_price = fields.Float(
        string="Expected Price",
        required=True,
    )

    selling_price = fields.Float(
        string="Selling Price",
        readonly=True,
        copy=False,
    )

    bedrooms = fields.Integer(
        string="Bedrooms",
        default=2,
    )

    living_area = fields.Integer(
        string="Living Area (sqm)",
        default=0,
    )

    facades = fields.Integer(
        string="Facades",
        default=0,
    )

    garage = fields.Boolean(string="Garage")

    garden = fields.Boolean(string="Garden")

    garden_area = fields.Integer(
        string="Garden Area (sqm)",
        default=0,
    )

    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        string="Garden Orientation",
    )

    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        default="new",
        copy=False,
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )

    total_area = fields.Integer(
        string="Total Area (sqm)",
        compute="_compute_total_area",
        store=True,
    )

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    price_per_sqm = fields.Float(
        string="Price per Square Meter",
        compute="_compute_price_per_sqm",
        store=True,
    )

    @api.depends("selling_price", "total_area")
    def _compute_price_per_sqm(self):
        for record in self:
            if record.total_area > 0:
                record.price_per_sqm = record.selling_price / record.total_area
            else:
                record.price_per_sqm = 0

