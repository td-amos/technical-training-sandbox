{
    # The name of the app as it will appear in Odoo
    "name": "Real Estate",  
    
    # The version of the app
    "version": "1.0",  
    
    # Other apps this app needs to work
    "depends": ["base", "contacts"],  
    
    # The person or company who made this app
    "author": "Amos",  
    
    # The category where this app will be listed in Odoo
    "category": "Real Estate",  
    
    # The license type for this app
    "license": "LGPL-3",  
    
    # A short description of what this app does
    "description": "App to manage real estate properties",  
    
    # Files that Odoo will load when the app is installed
    "data": [
        # File for setting user permissions
        "security/ir.model.access.csv",
        
        # File for creating the menu in Odoo
        "views/estate_menus.xml",
        
        # File for designing the screens (views) for properties
        "views/estate_property_views.xml",
    ],
    
    # Can this app be installed?
    "installable": True,  
    
    # Is this app a main app that shows in the Apps menu?
    "application": True,  
}