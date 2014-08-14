from django.shortcuts import render
from forms import ProjectSubmissionForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import ProjectSubmission, Project

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
	if request.method == 'POST':
		approved_submissions = request.POST.getlist('approved')
		disapproved_submissions = request.POST.getlist('disapproved')
		for submission in approved_submissions: #submission is unicode id
			print "submission: " + `submission`
			old = ProjectSubmission.objects.get(id=submission)
#			#submission description update by admin
#			name = 'description-' + str(submission)
#			old.description = request.POST.get(name)
			new = Project.objects.create()
			new.name = old.name
			new.email = old.email
			new.organization = old.organization
			new.website = old.website
			new.idea_name = old.idea_name
			new.description = old.description
			new.category = old.category
			new.image = old.image
			new.save()
			old.delete()
		for submission in disapproved_submissions:
			try: old = ProjectSubmission.objects.get(id=submission)
			except: continue
			old.delete()
		args = {}
		args.update(csrf(request))
		args['submissions'] = ProjectSubmission.objects.all()
		return render(request, 'admin_approve.html', args)
	return render(request, 'admin_approve.html', {'submissions':ProjectSubmission.objects.all()})