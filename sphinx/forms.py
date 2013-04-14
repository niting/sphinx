from django import forms
from sphinx.widgets import TagWidget
from sphinx.models import Answer
class AddQuestionForm(forms.Form):
	question = forms.CharField(widget=forms.widgets.Textarea(
		attrs={'rows':20, 'cols':80, 'class':
										'ui-widget ui-widget-content ui-corner-all'}))
	tags = forms.CharField(widget=TagWidget(attrs={'id':'add_question_tags','size':40,}))

class AddAnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('answer',)
		widgets = {
				'answer': forms.widgets.Textarea(attrs={'rows':40}),
		}

class AddTipForm(forms.Form):
	tip = forms.CharField(widget=forms.widgets.Textarea(
		attrs={'rows':10,'cols':80,'class':'ui-widget ui-widget-content ui-corner-all'}))
	tags = forms.CharField(widget=TagWidget(attrs={'id':'add_tip_tags','size':40,}))


