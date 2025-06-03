# Chapter 8: Computed Fields and Onchanges #

The relations between models are a key component of any Odoo module. 
They are necessary for the modelization of any business case. However, we may want links between the fields within a 
given model. Sometimes the value of one field is determined from the values of other fields and other times we want to 
help the user with data entry.

## Computed Fields
So far fields have been stored directly in and retrieved directly from the database. 
Fields can also be computed. In this case, the field’s value is not retrieved from the database 
but computed on-the-fly by calling a method of the model.

To create a computed field, create a field and set its attribute compute to the name of a method. 
The computation method should set the value of the computed field for every record in self.

By convention, compute methods are private, meaning that they cannot be called from the presentation tier, 
only from the business tier (see Chapter 1: Architecture Overview). 
Private methods have a name starting with an underscore _.


### Dependencies

The value of a computed field usually depends on the values of other fields in the computed record. 
The ORM expects the developer to specify those dependencies on the compute method with the `decorator depends()`. 
The given dependencies are used by the ORM to trigger the recomputation of the field whenever some of its dependencies
have been modified:

````from odoo import api, fields, models

class TestComputed(models.Model):
    _name = "test.computed"

    total = fields.Float(compute="_compute_total")
    amount = fields.Float()

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount

````
#### Note ####

`self` is a collection.

The object `self`  is a recordset, i.e. an ordered collection of records. 
It supports the standard Python operations on collections, e.g. `len(self)` and `iter(self)`, 
plus extra set operations such as `recs1 | recs2`.

Iterating over `self` gives the records one by one, where each record is itself a collection of size 1. 
You can access/assign fields on single records by using the dot notation, e.g. `record.name`.


### Inverse Function
You might have noticed that computed fields are read-only by default. 
This is expected since the user is not supposed to set a value. In some cases, it might be 
useful to still be able to set a value directly. In our real estate example, we can define a validity duration 
for an offer and set a validity date. We would like to be able to set either the duration or the 
date with one impacting the other.

To support this Odoo provides the ability to use an inverse function:
````
rom odoo import api, fields, models

class TestComputed(models.Model):
    _name = "test.computed"

    total = fields.Float(compute="_compute_total", inverse="_inverse_total")
    amount = fields.Float()

    @api.depends("amount")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount

    def _inverse_total(self):
        for record in self:
            record.amount = record.total / 2.0
````
A compute method sets the field while an inverse method sets the field’s dependencies.  
Note that the inverse method is called when saving the record, 
while the compute method is called at each change of its dependencies.

### Additional Information

Computed fields are not stored in the database by default. Therefore it is not possible 
to search on a computed field unless a search method is defined. 
This topic is beyond the scope of this training, so we won’t cover it. An example can be found here.

Another solution is to store the field with the `store=True` attribute. 
While this is usually convenient, pay attention to the potential computation load added to your model.

## Onchanges
In our real estate module, we also want to help the user with data entry. 
When the ‘garden’ field is set, we want to give a default value for the garden area as well as the orientation. 
Additionally, when the ‘garden’ field is unset we want the garden area to reset to zero and the orientation to be removed. 
In this case, the value of a given field modifies the value of other fields.

The ‘onchange’ mechanism provides a way for the client interface to update a form without saving anything to the 
database whenever the user has filled in a field value. To achieve this, we define a method where `self` represents the 
record in the form view and decorate it with `onchange()` to specify which field it is triggered by. 
Any change you make on self will be reflected on the form:
````
from odoo import api, fields, models

class TestOnchange(models.Model):
    _name = "test.onchange"

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    partner_id = fields.Many2one("res.partner", string="Partner")

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        self.name = "Document for %s" % (self.partner_id.name)
        self.description = "Default description for %s" % (self.partner_id.name)
````



### Additional Information
Onchanges methods can also return a non-blocking warning message.

## How to use them? ##