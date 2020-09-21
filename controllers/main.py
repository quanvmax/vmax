import datetime
import odoo

from odoo.http import request
from odoo import http, models, fields, _
from odoo.tools.misc import str2bool, xlwt
from odoo.addons.website.controllers.main import Website

class VmaxEcommerce(Website):
	# Home - Trang chủ - Anh Hồng
	@http.route('/', type='http', auth='public', website=True)
	def index(self, **kw):
		return request.render('vmax.homepage')

	# Shop - Trang danh sách sản phẩm - Anh Hồng
	@http.route('/shop', type='http', auth='public', website=True)
	def vmax_list_product(self, **kw):
		return request.render('vmax.list_product')

	# Shop/Detail - Trang chi tiết sản phẩm - Anh Hồng
	@http.route('/shop/product', type='http', auth='public', website=True)
	def vmax_product_details(self, **kw):
		return request.render('vmax.product_details')

	# Shop/Cart - Trang giỏ hàng - Anh Hồng
	@http.route('/shop/cart', type='http', auth='public', website=True)
	def vmax_cart(self, **kw):
		return request.render('vmax.cart')

	# Shop/Account - ??? - ???
	@http.route('/shop/account', type='http', auth='public', website=True)
	def vmax_account(self, **kw):
		return request.render('vmax.account')

	# Shop/Wishlist - Trang danh sách sản phẩm ưa thích - Quân
	@http.route('/shop/wishlist', type='http', auth='public', website=True)
	def vmax_wishlist(self, **kw):
		return request.render('vmax.wishlist')

	# Shop/Compare - Trang so sánh sản phẩm - Quân
	@http.route('/shop/compare', type='http', auth='public', website=True)
	def vmax_compare(self, **kw):
		return request.render('vmax.compare')

	# 404 - Trang báo lỗi 404 - Quân
	@http.route('/404', type='http', auth='public', website=True)
	def vmax_404(self, **kw):
		return request.render('vmax.404')
	
	# About Us - Trang giới thiệu về công ty - Quân
	@http.route('/aboutus', type='http', auth='public', website=True)
	def vmax_aboutus(self, **kw):
		return request.render('vmax.aboutus')

	# Contact - Trang liên hệ Vmax
	@http.route('/contact', type='http', auth='public', website=True)
	def vmax_contact(self, **kw):
		return request.render('vmax.contact')

	# Jobs - Trang tuyển dụng - Quân
	@http.route('/jobs', type='http', auth='public', website=True)
	def vmax_jobs(self, **kw):
		return request.render('vmax.jobs')

	# Job/Detail - Trang chi tiết công việc - Quân
	@http.route('/job/detail', type='http', auth='public', website=True)
	def vmax_job_detail(self, **kw):
		return request.render('vmax.job_detail')

	# Job/Apply - Trang ứng tuyển công việc - Quân
	@http.route('/job/apply', type='http', auth='public', website=True)
	def vmax_job_apply(self, **kw):
		return request.render('vmax.job_apply')

	# Job/Thanks - Trang cảm ơn vì đã ứng tuyển
	@http.route('/job/thanks', type='http', auth='public', website=True)
	def vmax_job_thanks(self, **kw):
		return request.render('vmax.job_thanks')

	# Blogs - Trang danh sách bài viết - Quân
	@http.route('/blogs', type='http', auth='public', website=True)
	def vmax_blogs(self, **kw):
		return request.render('vmax.blogs')

	# Blog/Detail - Trang bài viết - Quân
	@http.route('/blog/detail', type='http', auth='public', website=True)
	def vmax_blog_detail(self, **kw):
		return request.render('vmax.blog_detail')
