# Chapter 14: A Brief History of QWeb

So far the interface design of our real estate module has been rather limited. Building a list view is straightforward,
the same holds true for the form view. There is little to do in terms of design.

However, if we want to give a unique look to our application, it is necessary to go a step further 
and be able to design new views. 
Moreover, other features such as PDF reports or website pages need another tool to be created with more flexibility: 
a templating engine.

You might already be familiar with existing engines such as Jinja (Python), ERB (Ruby) or Twig (PHP). 
Odoo comes with its own built-in engine: QWeb Templates. QWeb is the primary templating engine used by Odoo. 
It is an XML templating engine and used mostly to generate HTML fragments and pages.