from oscar.apps.dashboard.catalogue import forms as base_forms

class ProductForm(base_forms.ProductForm):
	
	class Meta(base_forms.ProductForm.Meta):
	
		field = (
			'title', 'upc', 'on_sale',
			'short_description', 'description',
			'out_of_stock', 'bestseller',
			'is_new', 'is_discountable', 'structure',
			'markdown', 'markdown_reason')