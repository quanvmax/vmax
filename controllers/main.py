import datetime
import odoo

from odoo.http import request
from odoo import http, models, fields, _
from odoo.tools.misc import str2bool, xlwt
from odoo.addons.website.controllers.main import Website

class VmaxEcommerce(Website):

	@http.route('/', type='http', auth='public', website=True)
	def index(self, **kw):
		return request.render('vmax.homepage')

	@http.route('/shop', type='http', auth='public', website=True)
	def vmax_list_product(self, **kw):
		return request.render('vmax.list_product')

	@http.route('/shop/product', type='http', auth='public', website=True)
	def vmax_product_details(self, **kw):
		return request.render('vmax.product_details')

	@http.route('/shop/cart', type='http', auth='public', website=True)
	def vmax_cart(self, **kw):
		return request.render('vmax.cart')

	@http.route('/shop/account', type='http', auth='public', website=True)
	def vmax_account(self, **kw):
		return request.render('vmax.account')

	@http.route('/shop/wishlist', type='http', auth='public', website=True)
	def vmax_wishlist(self, **kw):
		return request.render('vmax.wishlist')