from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render

#def home(request):
#	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def media(request):
	return render(request, 'media.html')

def create(request):
	return render(request, 'create.html')