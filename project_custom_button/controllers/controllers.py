from odoo import http
from odoo.http import request

class SmsApi(http.Controller):

    @http.route('/button/check', type='http', auth='none', csrf=False, methods=['GET'])
    def index(self, **kw):
      return "<a href='https://github.com/abomsalam20/project_custom_button'  >github.com/abomsalam20/project_custom_button</a>"
   