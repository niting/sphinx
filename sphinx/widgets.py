from django.forms import widget

class TagWidget(widget.MultiValueField):
	"""Tagging widget to be rendered in a form"""
	    def __init__(self, attrs=None):
		    _widgets = (
				widgets.MultiValueWidget(attrs=attrs, att
			super(TagWidget, self).__init__(_widgets, attrs)

