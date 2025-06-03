## Chapter 3: Models and Basic Fields ##

### Object-Relational Mapping
Documentation related to this module can be 
found in: https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html#reference-orm-model

A key component of Odoo is the ORM layer.

Business objects are declared as Python classes extending Model, which integrates them into the automated
persistence system.

Models can be configured by setting attributes in their definition. 
The most important attribute is _name, which is required and defines 
the name for the model in the Odoo system. 
Here is a minimum definition of a model:
```aiignore
from odoo import models

class TestModel(models.Model):
    _name = "test_model"
```

Any modifications of the Python files requires a restart of the Odoo server.
When we restart the server, we can add the parameters `-d` and `-u`. `-d` means
that the upgrade must be performed on a particular database while `-u`
means we want to upgrade a module ie. the ORM will apply database schema changes.

### Model Fields
The documentation related to this topic can be found in
https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html#reference-orm-fields

#### Automatic Fields
You may have noticed your model has a few fields you never defined. 
Odoo creates a few fields in all models1. 
These fields are managed by the system and can’t be written to, 
but they can be read if useful or necessary:
- id
- create_date
- create_uid 
- write_date
- write_uid
