import datetime
import time
import netsvc
from openerp.tools.translate import _
from osv import osv, fields

class purchase_order(osv.osv):
	_inherit = "purchase.order"

purchase_order()


class purchase_order_line(osv.osv):
	_inherit = "purchase.order.line"

purchase_order_line()