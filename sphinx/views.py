from django.shortcuts import render_to_response
<<<<<<< HEAD
from django.template.context import RequestContext



def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
=======
from django.template import RequestContext
from sphinx.forms import AddQuestionForm
from django.http import HttpResponseRedirect
from sphinx.models import *
def index(request):
	return render_to_response('index.html', 
				context_instance=RequestContext(request))
>>>>>>> question

def add_question(request):
	if request.method == 'POST':
		form = AddQuestionForm(request.POST)
		if form.is_valid():
			question = request.POST['question']
			#Saving question first
			question_instance = Question(question=question, asked_by=request.user, votes=0)
			question_instance.save()
			tag_list = request.POST['tags'].split(',') 
			for tag in tag_list:
				#Saving tags now
				hash_val = 0
				tag = tag.lower()
				for c in tag:
					hash_val = 101 * hash_val + ord(hash_val)
				tag_instance = Tag(name=tag, tag_id=hash_val, popularity_score=0)
				tag_instance.save()
				tag_instance.question.add(question_instance)	 
			return HttpResponseRedirect('/show/question')
	else:
		form = AddQuestionForm()
	return render_to_response('add_question.html', {
								'form':form,
								}, 
							context_instance=RequestContext(request))
