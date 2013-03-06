from django.forms import widgets

class TagWidget(widgets.TextInput):
	"""Tagging widget to be rendered in a form"""
	class Media:
		css= {
				'all' : ('css/jquery.tagit.css',)
		}
		js = ('js/tag-it.js','js/common.js',)
		

