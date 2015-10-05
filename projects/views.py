from django.shortcuts import render, get_object_or_404
from forms import ProjectSubmissionForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import ProjectSubmission, Project
from django.db.models import Q
from accounts.models import UserProfile
from django.contrib.auth.models import User

############ ...create/... ####################
def create(request):
	if request.method == 'POST':
		form = ProjectSubmissionForm(request.POST, request.FILES, request=request)
		if form.is_valid():
#			form.owner = request.user
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
			#submission description update by admin
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
			new.url = old.url
			new.owner = old.owner
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

############ ...connect/... ################
def connect(request):
	category_filter = Q()
	projects_filter = Q()
	if 'category' in request.GET:
		category_filter |= Q(category=request.GET['category'])
	if 'project-search' in request.GET:
		query = request.GET['project-search']
		projects = Project.objects.filter(
										Q(name__icontains=query) & 
										category_filter
		).order_by()
		return render(request, 'connect.html', {'projects':projects, 'query':query})
	return render(request, 'connect.html', {'projects':Project.objects.all()})

def project_page(request, project_url):
	project = get_object_or_404(Project, url=project_url) #finds project object in database based on url. Very cool!
	context = {'project': project}
	context.update(csrf(request))
	profile=request.user.profile
	if request.method == 'GET':
		return render(request, 'project_page.html', context)
	elif 'join-project' in request.POST and request.POST['join-project'] == 'submit': #if join project, send email to project owner for approval and add request to table for approval
		project.member_requests.add(request.user)
		profile.member_requests.add(project)
		profile.save()
		#send_email to project owner/email(...)
		context['join'] = True
		return render(request, 'project_page.html', context)
	elif 'member-approve' in request.POST and request.POST['member-approve'] == 'submit':
		approved_requests = request.POST.getlist('approved')
		disapproved_requests = request.POST.getlist('disapproved')
		for member in approved_requests: #member is user id
			prof = UserProfile.objects.get(user_id=member)
			prof.projects.add(project)
			prof.save()
			u = User.objects.get(id=member)
			project.members.add(u)
			project.member_requests.remove(u)
			project.save()
			#send email...
		for member in disapproved_requests:
			u = User.objects.get(id=member)
			project.member_requests.remove(u)
			project.save()
		profile.member_requests.remove(project)
		return render(request, 'project_page.html', context)