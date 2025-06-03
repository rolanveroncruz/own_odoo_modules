# Chapter 7: Relations Between Models
However, in any real business scenario we need more than one model. 
Moreover, links between models are necessary. One can easily imagine one 
model containing the customers and another one containing 
the list of users. 
You might need to refer to a customer or a user on 
any existing business model.

## Many2One
Many2one is a type of field where many records of the model refer to 
a record of another model. 

For example, in the real estate module,
 A property type is, for example, a house or an apartment. 
A property type can have one type, but the same type can be assigned to many
properties.

A many2one is a simple link to another object. For example, in order to 
define a link to the res.partner in our test model, we can write:

````
partner_id = fields.Manyy2one("res.partner", string="Partner")
````
By convention, many2one fields have the `_id` suffix. Accessing the data
in the partner can then be easily done with:
````
print(my_test_object.partner_id.name)
````

## Many2Many
In our real estate module, we want to define the concept of property tags. 
A property tag is, for example, a property which is 
‘cozy’ or ‘renovated’.
  
A property can have many tags and a tag can be assigned to many properties. 
This is supported by the many2many concept.

A many2many is a bidirectional multiple relationship: any record on one side can be related 
to any number of records on the other side. For example, in order to define a link to the account.tax model 
on our test model, we can write: 
```
tax_ids = fields.Many2many("account.tax", string="Taxes")
```
By convention, many2many fields have the _ids suffix. This means that several taxes can be added to our test model. 
It behaves as a list of records, meaning that accessing the data must be done in a loop:
```
for tax in my_test_object.tax_ids:
    print(tax.name)
```
A list of records is known as a recordset, i.e. an ordered collection of records. 
It supports standard Python operations on collections, such as len() and iter(), 
plus extra set operations like recs1 | recs2.

## One2Many
A one2many is the inverse of a many2one. For example, we defined on our test model a link to the `res.partner` model 
thanks to the field partner_id. We can define the inverse relation, i.e. the list of test models linked to our partner:
```
test_ids = fields.One2many("test_model", "partner_id", string="Tests")
```
The first parameter is called the `comodel` and the second parameter is the field we want to inverse.

By convention, one2many fields have the _ids suffix. They behave as a list of records, 
meaning that accessing the data must be done in a loop:
```
for test in partner.test_ids:
    print(test.name)
```

 ### Danger ###

Because a One2many is a virtual relationship, there must be a Many2one field defined in the comodel.
