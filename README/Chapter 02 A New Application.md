## Chapter 2: A New Application ##

### The Real Estate Advertisement module

#### Prepare the addon folder.
1. The first step of module creation is to prepare its directory.
  The module directory should be created in a directory registered with _odoo.conf's
  addons_path_.
2. A module must contain at least 2 files: `__manifest__.py` and `__init__.py`. `__init.py__`
  can remain empty for now, but `__manifest__.py` file must describe the module and cannot 
  remain empty.Its only required field is `name` but usually contains much more information.

