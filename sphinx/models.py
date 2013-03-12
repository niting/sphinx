#TODO: Change the votes option to not be an integer field but
#TODO: rather a list of people who upvoted/downvoted
from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from model_utils import Choices
from django.core.urlresolvers import reverse


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

class Answer(models.Model):
	answer = models.TextField()
	answered_by = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	votes = models.IntegerField(default=0)

	class Meta:
		unique_together = (("answered_by", "question"),)

	def __unicode__(self):
		return self.answer

class Tip(models.Model):
	tip = models.CharField(max_length=200)
	tip_by = models.ForeignKey(User)
	votes = models.IntegerField(default=0)

	def get_absolute_url(self):
		return reverse('sphinx.views.tips_show', args=[str(self.id)])
		
	def __unicode__(self):
		return self.answer

class Tag(models.Model):
	""" Tag ID is a unique hash calculated from the tag string. We
		have a popularity score too for the popularity of a tag, which
		would help us with search results and getting maximum matches"""
	name = models.CharField(max_length=20)
	TAG_TYPE = Choices('college', 'company', 'topic', 'discipline', 'unknown')
	tag_type = models.CharField(choices=TAG_TYPE,
								default=TAG_TYPE.unknown, max_length=20)

	question = models.ManyToManyField(Question)
	popularity_score = models.IntegerField()	

	def __unicode__(self):
		return self.name
