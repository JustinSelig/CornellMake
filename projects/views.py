from django.shortcuts import render
from forms import ProjectSubmissionForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def create(request):
	if request.method == 'POST':
		form = ProjectSubmissionForm(request.POST, request.FILES, request=request)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('create_success'))
	args = {}
	args.update(csrf(request))
	args['form'] = ProjectSubmissionForm()
	return render(request, 'create.html', args)

def create_success(request):
	return render(request, 'create_success.html')