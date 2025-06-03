# Chapter 12: Inheritance


## Python Inheritance

In our real estate module, we never had to develop anything specific to be able to do the standard CRUD actions. 
The Odoo framework provides the necessary tools to do them. In fact, such actions are already included in our model 
thanks to classical Python inheritance:
```
from odoo import fields, models

class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"
```
Our class TestModel inherits from Model which provides create(), read(), write() and unlink().

These methods (and any other method defined on Model) can be extended to add specific business logic:
```
from odoo import fields, models

class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"

    ...

    @api.model
    def create(self, vals):
        # Do some business logic, modify vals...
        ...
        # Then call super to execute the parent method
        return super().create(vals)
```
The decorator `model()` is necessary for the `create()` method because the content of the recordset self is not relevant 
in the context of creation, but it is not necessary for the other CRUD methods.

It is also important to note that even though we can directly override the `unlink()` method, you will 
almost always want to write a new method with the decorator `ondelete()` instead. 
Methods marked with this decorator will be called during `unlink()` and avoids some issues that can occur 
during uninstalling the model’s module when `unlink()` is directly overridden.

In Python 3, `super()` is equivalent to `super(TestModel, self)`. 
The latter may be necessary when you need to call the parent method with a modified recordset.

## Danger ##

 It is very important to always call `super()` to avoid breaking the flow. There are only a few very specific cases where you don’t want to call it.
Make sure to always return data consistent with the parent method. For example, if the parent method returns a `dict()`, 
 your override must also return a `dict()`.

## Module Inheritance

In our real estate module, we would like to display the list of properties linked to a salesperson directly in the 
Settings / Users & Companies / Users form view. 
To do this, we need to add a field to the res.users model and adapt its view to show it.

Odoo provides two inheritance mechanisms to extend an existing model in a modular way.

The first inheritance mechanism allows modules to modify the behavior of a model defined in an another module by:

- adding fields to the model, 
- overriding the definition of fields in the model, 
- adding constraints to the model, 
- adding methods to the model, 
- overriding existing methods in the model.

The second inheritance mechanism (delegation) allows every record of a model to be linked to a parent model’s record 
and provides transparent access to the fields of this parent record.

In Odoo, the first mechanism is by far the most used. In our case, we want to add a field to an existing model, 
which means we will use the first mechanism. For example:
```
from odoo import fields, models

class InheritedModel(models.Model):
    _inherit = "inherited.model"

    new_field = fields.Char(string="New Field")

```
By convention, each inherited model is defined in its own Python file. 
In our example, it would be `models/inherited_model.py`.


## View Inheritance
Instead of modifying existing views in place (by overwriting them), Odoo provides view inheritance where children 
‘extension’ views are applied on top of root views. 
These extension can both add and remove content from their parent view.




























