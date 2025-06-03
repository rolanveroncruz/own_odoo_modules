# Chapter 13 Interact with Other Modules

In the previous chapter, we used inheritance to modify the behavior of a module. 
In our real estate scenario, we would like to go a step further and be able to generate invoices for our customers. 
Odoo provides an Invoicing module, so it would be neat to create an invoice directly from our real estate module, 
i.e. once a property is set to ‘Sold’, an invoice is created in the Invoicing application.


## Concrete Example: Account Move

Any time we interact with another module, we need to keep in mind the modularity. 
If we intend to sell our application to real estate agencies, some may want the invoicing feature 
but others may not want it.


### Link Module ###
The common approach for such use cases is to create a ‘link’ module. 
In our case, the module would depend on estate and account and would include the invoice creation logic of the 
estate property. 
This way the real estate and the accounting modules can be installed independently. 
When both are installed, the link module provides the new feature.

When the estate_account module appears in the list, 
go ahead and install it! You’ll notice that the Invoicing application is installed as well. 
This is expected since your module depends on it. 
If you uninstall the Invoicing application, your module will be uninstalled as well.

### Invoice Creation ###
It’s now time to generate the invoice. We want to add functionality to the estate.property model, i.e. 
we want to add some extra logic for when a property is sold. Does that sound familiar? 
If not, it’s a good idea to go back to the previous chapter since you might have missed something ;-)



