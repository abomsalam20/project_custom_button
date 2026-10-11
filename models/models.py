
from odoo import models, fields, api
import requests

import json


class project_task(models.Model):
    _inherit = 'project.task'
 
    
    def open_url(self):
            return {
             'type': 'ir.actions.act_url',
            'url': 'https://github.com/abomsalam20/project_custom_button',
            'target': 'new', # Use 'new' for a new tab, or 'self' to replace current page
         }

   