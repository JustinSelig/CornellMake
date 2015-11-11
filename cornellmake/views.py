from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render
from projects.models import Project

#def home(request):
#	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def home(request):
	projects = Project.objects.all()[:3]	#change to be most popular projects
	return render(request, 'index.html', {'projects':projects})

#def discover(request):
#	if 'project-search' in request.GET:
#		query = request.GET['project-search']
#		projects = Project.objects.filter(name__icontains=query)
#		return render(request, 'discover.html', {'projects':projects, 'query':query})
#	return render(request, 'discover.html')
