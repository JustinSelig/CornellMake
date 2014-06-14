from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render

"""Returns an HttpResponse with string as Template"""
def home(request):
	return render(request, 'index.html')