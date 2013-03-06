from django import forms
from sphinx.widgets import TagWidget

class AddQuestionForm(forms.Form):
	question = forms.CharField(widget=forms.widgets.Textarea(
		attrs={'rows':20, 'cols':80, 'class':
										'ui-widget ui-widget-content ui-corner-all'}))
	tags = forms.CharField(widget=TagWidget(attrs={'id':'add_question_tags','size':40,}))
