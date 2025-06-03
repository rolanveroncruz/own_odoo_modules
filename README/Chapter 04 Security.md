## Chapter 4: Security - A Brief Introduction

In a business application such as Odoo, one of the first questions to consider 
is who can access the data. Odoo provides a security mechanism to 
allow access to the data for specific groups of users.

This chapter aims to cover the minimum required for our new module.
More detail is covered here: https://www.odoo.com/documentation/18.0/developer/tutorials/restrict_data_access.html

Data files related to security is located in the `security` folder.
### Access Rights
Documentation for this topic can be found here:
https://www.odoo.com/documentation/18.0/developer/reference/backend/security.html#reference-security-acl

When no access rights are defined on a model, 
Odoo determines that no users can access the data. 
It is even notified in the log:

Access rights are defined as records of the model `ir.model.access`.
Each access right is associated with a model, a group (or no group for global access) 
and a set of permissions: create, read, write and unlink2. 
Such access rights are usually defined in a CSV file named `ir.model.access.csv`.