from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')

def add_question(request, question, tags):
		
	return render_to_response('add_question.html')
