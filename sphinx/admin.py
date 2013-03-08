from django.contrib import admin
from sphinx.models import Question

class QuestionAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.asked_by = request.user
		obj.save()

admin.site.register(Question, QuestionAdmin)
