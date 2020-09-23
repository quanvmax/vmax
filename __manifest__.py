# -*- coding: utf-8 -*-
{
	"name"                 :  "Theme Vmax",
	"category"             :  "Theme/eCommerce",
	"version"              :  "1.0",
	"sequence"             :  1,
	"author"               :  "Fresher",
	"license"              :  "Other proprietary",
	"description"          :  """Giao diện website Odoo Vmax - Mực in và máy in văn phòng chính hãng.""",
	"depends" : ['website', 'website_theme_install', 'sale', 'website_sale', 'website_sale_wishlist'],
	"data" : [
		'views/assets.xml',
		'views/header.xml',
		'views/footer.xml',
		'views/homepage.xml',
		'views/product.xml',
		'views/list_product.xml',
		'views/cart.xml',
		'views/account.xml',
		'views/wishlist.xml',
		'views/compare.xml',
		'views/404.xml',
		'views/aboutus.xml',
		'views/contact.xml',
		'views/jobs.xml',
		'views/job_detail.xml',
		'views/job_apply.xml',
		'views/job_thanks.xml',
		'views/blogs.xml',
		'views/blog_detail.xml',
		'views/compare.xml'
	],
	"images" : [
		'static/src/img/vmax_screenshot.jpg',
	],
	"application"          :  False,
	"installable"          :  True,
}