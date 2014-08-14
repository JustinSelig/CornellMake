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
#			obj.description = request.POST.get(name)
#			obj.save()
			new = Project.objects.create()
#			new.user_id = obj.user_id
			new.name = old.name
			new.email = old.email
			new.organization = old.organization
			new.website = old.website
			new.idea_name = old.idea_name
			new.description = old.description
			new.category = old.category
			new.image = old.image
#			increase = new.approve()
			new.save()
			old.delete()
		for submission in disapproved_submissions:
			old = ProjectSubmission.objects.get(id=submission)
#			#user =  User.objects.get(id=obj.user_id)
#			obj.disapprove()
			old.delete()
		args = {}
		args.update(csrf(request))
		args['submissions'] = ProjectSubmission.objects.all()
		return render(request, 'admin_approve.html', args)
	return render(request, 'admin_approve.html', {'submissions':ProjectSubmission.objects.all()})