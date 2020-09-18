# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductDes(models.Model):
	_inherit = 'product.template'

	vm_description_product = fields.Html('Description')