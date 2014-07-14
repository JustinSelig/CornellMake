from django.shortcuts import render
from forms import ProductForm

def create(request):
	args = {}
	args['form'] = ProductForm()
	return render(request, 'create.html', args)