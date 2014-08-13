from django.shortcuts import render
from forms import ProjectSubmissionForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import ProjectSubmission

def create(request):
	if request.method == 'POST':
		form = ProjectSubmissionForm(request.POST, request.FILES, request=request)
		if form.is_valid():
			form.save()
#			return HttpResponseRedirect(reverse('create'))
			return render(request, 'create.html', {'success':True})
	args = {}
	args.update(csrf(request))
	args['form'] = ProjectSubmissionForm()
	return render(request, 'create.html', args)

def approve(request):
	return render(request, 'admin_approve.html', {'submissions':ProjectSubmission.objects.all()})