# -*- coding: utf-8 -*-
#from osv import fields, osv

import math
import re
import logging
import openerp.addons.decimal_precision as dp
#import openerp.addons.product.pricelist

#from _common import rounding
from openerp import tools
from openerp.osv import osv, fields
from openerp.tools.translate import _


_logger = logging.getLogger(__name__) # Need for message in console.



class product_template(osv.osv):
    _name = 'product.template'
    _inherit = 'product.template'
    _columns = {
         # For display price in product.
        'prices_ids': fields.one2many('product.pricelist.item', 'product_tmpl_id', 'Supplier'),
       # 'retail_price': fields.float('Retail Price', digits_compute=dp.get_precision('Product Price'), help="Retail price."),

        }



class product_pricelist_item(osv.osv):
    _name = 'product.pricelist.item'
    _inherit = 'product.pricelist.item'
    _columns = {


        }

product_pricelist_item()











