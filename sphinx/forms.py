from django import forms

class AddQuestionForm(forms.Form):
	question = forms.CharField(widget=forms.TextInput(
									attrs={'size':40, 
										'class':
										'ui-widget ui-widget-content ui-corner-all'}))
	tags = forms.CharField()
