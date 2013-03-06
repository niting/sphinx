from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from model_utils import Choices
from django.core.urlresolvers import reverse

class BigIntegerField(models.IntegerField):
	empty_strings_allowed = False
	def get_internal_type(self):
		return "BigIntegerField"
	def db_type(self, connection):
		return 'bigint'

class Question(models.Model):
	question = models.TextField()
	asked_by = models.ForeignKey(User, null=True, blank=True, related_name='asked_by')
	votes = models.IntegerField()
	def get_absolute_url(self):
		return reverse('sphinx.views.questions_show', args=[str(self.id)])

class Comment(models.Model):
	comment = models.TextField()
	comment_by = models.ForeignKey(User)
	question = models.ForeignKey('Question')

class Tag(models.Model):
	""" Tag ID is a unique hash calculated from the tag string. We
		have a popularity score too for the popularity of a tag, which
		would help us with search results and getting maximum matches"""
	name = models.CharField(max_length=20)
	tag_id = BigIntegerField(primary_key=True)
	TAG_TYPE = Choices('college', 'company', 'topic', 'discipline', 'unknown')
	tag_type = models.CharField(choices=TAG_TYPE,
								default=TAG_TYPE.unknown, max_length=20)

	question = models.ManyToManyField(Question)
	popularity_score = models.IntegerField()	
