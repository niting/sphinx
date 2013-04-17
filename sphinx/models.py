#TODO : Add commenting features
from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices
from django.core.urlresolvers import reverse

class Tag(models.Model):
	""" Tag ID is a unique hash calculated from the tag string. We
		have a popularity score too for the popularity of a tag, which
		would help us with search results and getting maximum matches"""
	name = models.CharField(max_length=20, unique=True)
	TAG_TYPE = Choices('college', 'company', 'topic', 'discipline', 'unknown')
	tag_type = models.CharField(choices=TAG_TYPE,
								default=TAG_TYPE.unknown, max_length=20)
	popularity_score = models.IntegerField()	

	def __unicode__(self):
		return self.name

"""Items which are votable come here first"""
class Votable(models.Model):
	up_votes = models.IntegerField()
	down_votes = models.IntegerField()
	upvotes_by = models.ManyToManyField(User, related_name='%(class)s_upvotes_by')
	downvotes_by = models.ManyToManyField(User, related_name='%(class)s_downvotes_by')
	author = models.ForeignKey(User, null=True, blank=True, related_name='%(class)s_author')
	time = models.DateTimeField(auto_now=True)
	tags = models.ManyToManyField(Tag, related_name='%(class)s_tags')

	class Meta:
		abstract = True


class Question(Votable):
	question = models.TextField()

	def get_absolute_url(self):
		return reverse('sphinx.views.questions_show', args=[str(self.id)])

	def __unicode__(self):
		return self.question

class Answer(Votable):
	answer = models.TextField()
	question = models.ForeignKey(Question)

	class Meta:
		unique_together = (("author", "question"),)

	def __unicode__(self):
		return self.answer

class Tip(Votable):
	tip = models.CharField(max_length=200)

	def get_absolute_url(self):
		return reverse('sphinx.views.tips_show', args=[str(self.id)])
		
	def __unicode__(self):
		return self.tip

class Experience(Votable):
	experience = models.TextField()

	def __unicode__(self):
		return self.experience

"""Votable ends here"""

