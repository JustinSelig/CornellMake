from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render
from projects.models import Project

#def home(request):
#	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def media(request):
	return render(request, 'media.html')

def connect(request):
	if 'query' in request.GET:
		query = request.GET['query']
		projects = Project.objects.filter(name__icontains=query)
		return render(request, 'connect.html', {'projects':projects, 'query':query})
	return render(request, 'connect.html')