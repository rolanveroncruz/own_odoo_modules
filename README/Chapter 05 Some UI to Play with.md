## Chapter 5: Finally, Some UI to Play With

### Data Files
For loading complex data, instead of using CSV, we use XML.
In Odoo, the user interface (actions, menus, views) is largely defined by creating and composing records defined in an
XML file. A common pattern is Menu > Action > View. To access records, the user navigates through several menu levels;
the deepest level is action which triggers the opening of a list of records.

### Actions
From (https://www.odoo.com/documentation/18.0/developer/reference/backend/actions.html):
Actions define the behavior of the system in response to user actions: login, action buttons, selection of an invoice, ...
Actions can be stored in the database or returned directly as dictionaries in e.g. button methods.
All actions share two mandatory attributes:
-type - the category of the current action, determines which fields may be used and how the action is interpreted
-name - short user-readable description of the action, may be displayed in the client's interface

A client can get actions in 4 forms:
- False - if any action dialog is currently open, close it
- A string - if a `client action` matches, interpret as a client action's tag, otherwise treat as a number
- A number - read the corresponding action record from the database, may be a database identifier or an external id
- A dictionary - treat as a client action descriptor and execute

### Menus
From (https://www.odoo.com/documentation/18.0/developer/reference/backend/data.html#reference-data-shortcuts):
Because some important structural models of Odoo are complex and involved, data files provide shorter alternatives to 
defining them using `record tags`:

 - `menuitem` - defines an `ir.ui.menu` record wih a number of defaults and feedbacks: 
