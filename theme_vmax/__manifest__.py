# -*- coding: utf-8 -*-
{
	"name"                 :  "Vmax",
	"category"             :  "Theme/eCommerce",
	"version"              :  "1.0",
	"sequence"             :  10,
	"author"               :  "Xuan Hong",
	"license"              :  "Other proprietary",
	"description"          :  """Giao diện website Vmax - Mực in, máy in chính hãng.""",
	"depends" : ['website', 'sale_management', 'website_sale', 'mail', 'website_sale_wishlist'],
	"data" : [
		'views/assets.xml',
		'views/header.xml',
		'views/footer.xml',
		'views/homepage.xml',
		'views/products.xml',
		'views/cart.xml',
		'views/auth_signup_login.xml',
		'views/404.xml',
		'views/s_home_services.xml',
		'views/snippets.xml',
		'views/product_view.xml',
		'views/website_template.xml',
	],
	"images" : [
		'static/src/img/vmax_screenshot.jpg',
	],
	"application" :  False,
	"installable" :  True,
	'auto_install': True,
}