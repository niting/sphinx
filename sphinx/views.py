from django.shortcuts import render_to_response
from django.template.context import RequestContext
from sphinx.forms import AddQuestionForm
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
				hash_val = 0
				tag = tag.lower()
				for c in tag:
					hash_val = 101 * hash_val + ord(c)
				tag_instance = Tag(name=tag, tag_id=hash_val, popularity_score=0)
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
	return render_to_response('questions_show.html', {'question' : 'Test', 'tags':['dadd','asdad',]}, context_instance=RequestContext(request))
