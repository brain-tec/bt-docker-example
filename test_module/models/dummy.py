from odoo import models, fields, api, _  # '_' is unused and should be removed

class DummyModel(models.Model):
    _name = 'dummy.model'
    
    name = fields.Char(string='Name', required=True)

    # This method is missing the 'self' parameter.
    def method_without_self():  
        # Intentionally written incorrect to simulate an error.
        print("This method should have self as its first parameter.")

    @api.model
    def compute_something(self):
         # Spacing errors that a formatter like ruff might fix:
         x=1+2  
         # List comprehension with extra spaces
         y = [ i for i in range(10) if i>5 ]
         # Unused variable (could be flagged for removal)
         unused_var = 42  
         return x, y
