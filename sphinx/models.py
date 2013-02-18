from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from model_utils import Choices

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	score = models.PositiveIntegerField()

class Question(models.Model):
	question = models.TextField()
	asked_by = models.ForeignKey('UserProfile')
	votes = models.IntegerField()
	
class Comment(models.Model):
	comment = models.TextField()
	comment_by = models.ForeignKey('UserProfile')
	question = models.ForeignKey('Question')

class Tag(models.Model):
	name = models.CharField(max_length=20)
	TAG_TYPE = Choices('college', 'company', 'topic', 'discipline', 'unknown')
	tag_type = models.CharField(choices=TAG_TYPE,
								default=TAG_TYPE.unknown, max_length=20)

	question = models.ManyToManyField(Question)
	
