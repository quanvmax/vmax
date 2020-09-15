import datetime
import odoo

from odoo.http import request
from odoo import http, models, fields, _
from odoo.tools.misc import str2bool, xlwt
from odoo.addons.website.controllers.main import Website

class HomepageVmax(Website):
	@http.route()
	def index(self, **kw):
		super(HomepageVmax, self).index()

		Products = request.env['product.template'].sudo()
		
		mucin = Products.search([('public_categ_ids.id', 'child_of', 1)], limit=4)
		mayin = Products.search([('public_categ_ids.id', 'child_of', 8)], limit=4)
		website_product_ids = request.env['product.template'].sudo().search([('is_published', '=', True)], limit=8)
		
		data = {
			'website_product_ids' : website_product_ids,
			'mucin' : mucin,
			'mayin' : mayin
		}
		return request.render('theme_vmax.vm_homepage', data)