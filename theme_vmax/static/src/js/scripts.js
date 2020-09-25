odoo.define('theme_vmax.custom', function (require) {
	'use strict';

var base = require('web_editor.base');
var ajax = require('web.ajax');

	base.ready().then(function() {
		
		$('.btn-more').on('click', function(ev){
			$('.More').switchClass('More' ,'Full');
			$('.Full').switchClass('Full' ,'More');
		});

		$('#owl_best').owlCarousel({
		    loop:true,
		    margin:10,
		    nav:true,
		    navText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
		    dots: false,
			autoplay:true,
			autoplayTimeout:3000,
			autoplayHoverPause:true,
		    responsive:{
		        0:{
		            items:1
		        },
		        600:{
		            items:3
		        },
		        1000:{
		            items:5
		        }
		    }
		})

		$('#owl_brands').owlCarousel({
		    loop:true,
		    margin:10,
		    nav:false,
		    dots: false,
			autoplay:true,
			autoplayTimeout:5000,
			autoplayHoverPause:true,
		    responsive:{
		        0:{
		            items:1
		        },
		        600:{
		            items:3
		        },
		        1000:{
		            items:5
		        }
		    }
		})
	});
});