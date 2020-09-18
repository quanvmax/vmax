import datetime
import odoo

from odoo.http import request
from odoo import http, models, fields, _
from odoo.tools.misc import str2bool, xlwt
from odoo.addons.website.controllers.main import Website

class WebsiteVmax(Website):
	@http.route('/', type='http', auth="public", website=True)
	def index(self, **kw):
		super(WebsiteVmax, self).index()

		Products = request.env['product.template'].sudo()
		
		All_product = Products.sudo().search([('is_published', '=', True)], limit=8)
		#Mucin = Products.search([('public_categ_ids.id', 'child_of', 1)], limit=4)
		#Mayin = Products.search([('public_categ_ids.id', 'child_of', 8)], limit=4)
		
		data = {
			'website_product_ids' : All_product,
			#'mucin' : Mucin,
			#'mayin' : Mayin
		}
		return request.render('theme_vmax.vm_homepage', data)

	@http.route('/ve-vmax', type='http', auth='public', website=True)
	def aboutus(self, **kw):
		return request.render('theme_vmax.aboutus')