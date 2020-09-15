# -*- coding: utf-8 -*-
{
	"name"                 :  "Vmax",
	"category"             :  "Theme/eCommerce",
	"version"              :  "1.0",
	"sequence"             :  1,
	"author"               :  "Xuan Hong",
	"license"              :  "Other proprietary",
	"description"          :  """Giao diện website Vmax - Mực in, máy in chính hãng.""",
	"depends" : ['website', 'website_theme_install', 'sale', 'website_sale', 'website_sale_wishlist'],
	"data" : [
		'views/assets.xml',
		'views/header.xml',
		'views/footer.xml',
		'views/homepage.xml',
		'views/products.xml',
		'views/s_home_services.xml',
		'views/snippets.xml',
	],
	"images" : [
		'static/src/img/vmax_screenshot.jpg',
	],
	"application"          :  False,
	"installable"          :  True,
}