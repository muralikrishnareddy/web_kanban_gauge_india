# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import os
import re
import openerp
from openerp import SUPERUSER_ID, tools
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools.safe_eval import safe_eval as eval
from openerp.tools import image_resize_image
  
class sales_team(osv.osv):
    _inherit = "crm.case.section"
   
    def _get_decimals(self, cr, uid, context=None):
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        return user.company_id.sales_team_decimals
        
    def _get_decimals_team(self, cr, uid, ids, field_name, arg, context=None):
        res = dict.fromkeys(ids, 0)
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        for line in self.browse(cr, uid, ids, context=context):
            res[line.id] = user.company_id.sales_team_decimals
        return res
        
    _columns = {
        'sales_team_decimals': fields.function(_get_decimals_team, type='integer', string='Digits'),
    }
    #_defaults = {
    #    'sales_team_decimals':lambda s, cr, uid, c: s._get_decimals(cr, uid, c),
    #}
    
sales_team()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


