odoo.define('theme_vmax.custom', function (require) {
	'use strict';

var base = require('web_editor.base');
var ajax = require('web.ajax');

	base.ready().then(function() {
		$('.btn-more').on('click', function(ev){
			$('.More').switchClass('More' ,'Full');
			$('.Full').switchClass('Full' ,'More');
			
		});
	});
});