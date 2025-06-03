from dateutil.relativedelta import relativedelta

from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name=fields.Char('Property Name', required=True, default="Unknown")
    description=fields.Text('Property Description')
    postcode=fields.Char('Postcode')
    date_available=fields.Date('Date Available', copy=False, default=fields.Date.today() + relativedelta(months=3) )
    expected_price=fields.Float('Expected Price', required=True)
    selling_price=fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms=fields.Integer('Bedrooms', default=2)
    living_area=fields.Integer('Living Area')
    facades=fields.Integer('Facades')
    garage=fields.Boolean('Garage')
    garden=fields.Boolean('Garden')
    garden_area=fields.Integer('Garden Area')
    garden_orientation=fields.Selection([('north', 'North'),('south', 'South'), ('east', 'East'),('west', 'West') ],'Garden Orientation')
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    property_type = fields.Many2one('estate.property.type', 'Property Type')
    active = fields.Boolean('Active', default=True)
    state=fields.Selection([('new', 'New'),('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
                            ('sold', 'Sold'), ('cancelled', 'Cancelled') ],'State')
    buyer = fields.Many2one('res.users', 'Buyer', copy=False)
    salesperson = fields.Many2one('res.users', string='Sales Person', default=lambda self: self.env.user)
    tags = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.Many2many('estate.property.offer', string='Offers')


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'

    name = fields.Char('Tag Name', required=True, default="Unknown")
    description= fields.Char('Tag Description', required=True, default="None")


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    type_name = fields.Char('Property Type', required=True)
    description = fields.Text('Property Description')



class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offer'

    price=fields.Float('Price')
    status=fields.Selection([('accepted','Accepted'), ('refused','Refused')],'Offer Status')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
