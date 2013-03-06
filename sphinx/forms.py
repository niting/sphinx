from django import forms
from sphinx.widgets import TagWidget
class AddQuestionForm(forms.Form):
	question = forms.CharField(widget=forms.TextInput(
									attrs={'size':40, 
										'class':
										'ui-widget ui-widget-content ui-corner-all'}))
	tags = forms.CharField(widget=TagWidget(attrs={'size':40,}))
