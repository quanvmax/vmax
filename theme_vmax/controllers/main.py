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

		Category = request.env['product.public.category']
		Products = request.env['product.template']
		
		All_product = Products.sudo().search([('is_published', '=', True)], limit=8)
		Best_seller = Products.sudo().search([('is_published', '=', True)], limit=5)
		Category_menu = Category.sudo().search([], limit=5)
		#Mucin = Products.search([('public_categ_ids.id', 'child_of', 1)], limit=4)
		#Mayin = Products.search([('public_categ_ids.id', 'child_of', 8)], limit=4)
		
		data = {
			'products' : All_product,
			'best_sellers' : Best_seller,
			'categories' : Category_menu,
			#'mucin' : Mucin,
			#'mayin' : Mayin
		}
		return request.render('theme_vmax.vm_homepage_new', data)

	# About Us - Trang giới thiệu về công ty - Quân
	@http.route('/aboutus', type='http', auth='public', website=True)
	def vmax_aboutus(self, **kw):
		return request.render('theme_vmax.aboutus')

	# Contact - Trang liên hệ Vmax
	@http.route('/contact', type='http', auth='public', website=True)
	def vmax_contact(self, **kw):
		return request.render('theme_vmax.contact')

	# Jobs - Trang tuyển dụng - Quân
	@http.route('/tuyen-dung', type='http', auth='public', website=True)
	def vmax_jobs(self, **kw):
		jobs = request.env['hr.job'].sudo().search([])
		return request.render("theme_vmax.jobs", {"jobs" : jobs})

	# Job/Detail - Trang chi tiết công việc - Quân
	@http.route('/tuyen-dung/chi-tiet', type='http', auth='public', website=True)
	def vmax_job_detail(self, **kw):
		return request.render('theme_vmax.job_detail')

	# Job/Apply - Trang ứng tuyển công việc - Quân
	@http.route('/tuyen-dung/ung-tuyen', type='http', auth='public', website=True)
	def vmax_job_apply(self, **kw):
		return request.render('theme_vmax.job_apply')

	# Job/Thanks - Trang cảm ơn vì đã ứng tuyển
	@http.route('/tuyen-dung/cam-on', type='http', auth='public', website=True)
	def vmax_job_thanks(self, **kw):
		return request.render('theme_vmax.job_thanks')

	# Blogs - Trang danh sách bài viết - Quân
	@http.route('/blogs', type='http', auth='public', website=True)
	def vmax_blogs(self, **kw):
		return request.render('theme_vmax.blogs')

	# Blog/Detail - Trang bài viết - Quân
	@http.route('/blogs/detail', type='http', auth='public', website=True)
	def vmax_blog_detail(self, **kw):
		return request.render('theme_vmax.blog_detail')

	# Shop/Wishlist - Trang danh sách sản phẩm ưa thích - Quân
	@http.route('/san-pham-yeu-thich', type='http', auth='public', website=True)
	def vmax_wishlist(self, **kw):
		return request.render('theme_vmax.wishlist')

	# Shop/Compare - Trang so sánh sản phẩm - Quân
	@http.route('/so-sanh-san-pham', type='http', auth='public', website=True)
	def vmax_compare(self, **kw):
		return request.render('theme_vmax.compare')