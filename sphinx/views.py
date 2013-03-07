from django.shortcuts import render_to_response
from django.template.context import RequestContext
from sphinx.forms import AddQuestionForm
from sphinx.forms import AddAnswerForm
from django.http import HttpResponseRedirect
from sphinx.models import *

def index(request):
	return render_to_response('index.html', 
				context_instance=RequestContext(request))


def questions_add(request):
	if request.method == 'POST':
		form = AddQuestionForm(request.POST)
		if form.is_valid():
			question = request.POST['question']
			#Saving question first
			question_instance = Question(question=question, votes=0)
			question_instance.asked_by = request.user
			question_instance.save()
			tag_list = request.POST['tags'].split(',') 
			for tag in tag_list:
				#Saving tags now
				tag = tag.lower()
				tag_instance = Tag(name=tag, popularity_score=0)
				tag_instance.save()
				tag_instance.question.add(question_instance)	 
			return HttpResponseRedirect(question_instance.get_absolute_url())
	else:
		form = AddQuestionForm()
	return render_to_response('questions_add.html', {
								'form':form,
								}, 
							context_instance=RequestContext(request))

def questions_show(request, question_id):
	if request.method == 'POST':
		form = AddAnswerForm(request.POST)
		if form.is_valid():
			answer_instance = form.save(commit = False)
			answer_instance.question = Question.objects.get(pk=question_id)
			answer_instance.answered_by = request.user
			answer_instance.save()
	else:
		form = AddAnswerForm()
	
	question = Question.objects.get(pk=question_id)
	answer_added = True
	try:
		answer_instance = Answer.objects.get(answered_by=request.user, question=question)
	except Answer.DoesNotExist:
		answer_added = False

	return render_to_response('questions_show.html', 
								{'question' : question, 
								'tags':question.tag_set.all(),
								'answers':question.answer_set.all(),
								'form':form,
								'answer_added':answer_added}, 
								context_instance=RequestContext(request))
