## Chapter 1: Architecture Overview ##
### Multitier Application
This chapter discusses that Odoo follows a _multitier architecture_, that is, it has:
- a presentation tier - to translate tasks and results to something the use can understand
- logic tier - coordinates the application, processes commands, makes decisions, and moves and processes data betwwn the
  two other layers
- data tier stores and retrieves information from a database

### Odoo Modules
Both server and client extensions are packaged as modules which are optionally loaded in a _database_.
A _module_ is a collection of functions and data that target a single purpose.

Odoo modules can either add brand new business logic to an Odoo system or alter and extend existing business logic.
One module can be created to add your country’s accounting rules to Odoo’s generic accounting support,
while a different module can add support for real-time visualisation of a bus fleet.

#### Composition of a module ####

An odoo module can contain a number of elements:
- Business objects
- Object views
- Data files
- Web controllers
- Static web data

#### Module Structure
Each module is a directory within a _module directory_. Module directories are
specified using the _--addons-path_ option.

An Odoo module is declared  by its _manifest_.

