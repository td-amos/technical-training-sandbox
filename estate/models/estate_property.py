    # Import the required modules from Odoo
from odoo import models, fields

# Define a new model for storing real estate property details
class EstateProperty(models.Model):
    _name = "estate.property"  # This is the technical name of the model (table name in the database)
    _description = "Real Estate Property"  # A short description of the model

    # Defining fields (columns in the database)
    name = fields.Char(
        string="Title",  # Human-readable name for the field (used in UI)
        required=True,  # This makes the field mandatory
    )

    description = fields.Text(
        string="Description"  # A long text field for extra details
    )

    postcode = fields.Char(
        string="Postcode"  # Stores the postal code of the property location
    )

    date_availability = fields.Date(
        string="Available From"  # Date field to store when the property will be available
    )

    expected_price = fields.Float(
        string="Expected Price",  # Stores the asking price of the property
        required=True,  # This makes sure that a price must be set
    )

    selling_price = fields.Float(
        string="Selling Price",  # Stores the final selling price
        readonly=True,  # This field cannot be edited manually
        copy=False,  # Prevents the value from being copied when duplicating a record
    )

    bedrooms = fields.Integer(
        string="Bedrooms",  # Stores the number of bedrooms
        default=1,  # If not specified, it defaults to 1 bedroom
    )

    living_area = fields.Integer(
        string="Living Area (sqm)"  # Stores the size of the living area in square meters
    )

    facades = fields.Integer(
        string="Facades"  # Number of external sides (facades) of the house
    )

    garage = fields.Boolean(
        string="Garage"  # Boolean field (True/False) to indicate if a garage is present
    )

    garden = fields.Boolean(
        string="Garden"  # Boolean field to indicate if the property has a garden
    )

    garden_area = fields.Integer(
        string="Garden Area (sqm)"  # Stores the size of the garden in square meters
    )

    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        string="Garden Orientation",  # Stores the direction the garden faces
    )

# This will create a table 'estate_property' in the database with all the above fields.
