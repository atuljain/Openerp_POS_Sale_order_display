import logging
import time
from openerp import netsvc, tools, pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import SUPERUSER_ID

import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class pos_sale_invoiced(osv.osv):
  _name = 'pos.sale.invoiced'
  _order = 'sale_order asc'
  _columns ={
            'sale_order':fields.one2many('sale.order', 'order_id', Sale Order, states={'invoiced':[('readonly', True)]}),
            
              }
