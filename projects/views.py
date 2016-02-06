from django.shortcuts import render, get_object_or_404, render_to_response
from forms import ProjectSubmissionForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import ProjectSubmission, Project
from django.db.models import Q
from accounts.models import UserProfile
from django.contrib.auth.models import User

############ ...create/... ####################
def create(request):	#initial screen asking for project name and category
	if request.POST and 'submit-initial' in request.POST: #submitted initial form, 'submit-initial' is in name field
		args = {}
		args["category"] = request.POST.get("category")
		args["project_name"] = request.POST.get("project_name")		
		args.update(csrf(request))
		args['form'] = ProjectSubmissionForm()
		args['form'] = ProjectSubmissionForm()
		return render(request, 'create-form.html', args)
	elif request.POST and 'submit-final' in request.POST: #actual full form submitted
		form = ProjectSubmissionForm(request.POST, request.FILES, request=request)
		if form.is_valid():
#			form.owner = request.user
			form.save()
#			return HttpResponseRedirect(reverse('create'))
			return render(request, 'create-form.html', {'success':True})
		#else: return render(request, 'about.html') #uncomment to test form validity
		return render(request, 'discover.html') #if form is invalid take to discover page
	return render(request, 'create.html')

"""
def create_form(request):	#full project form
	if request.method == 'POST': #submitted full project form
		form = ProjectSubmissionForm(request.POST, request.FILES, request=request)
		if form.is_valid():
#			form.owner = request.user
			form.save()
#			return HttpResponseRedirect(reverse('create'))
			return render(request, 'index.html', {'success':True})
	args = {}	#
	args.update(csrf(request))
	args['form'] = ProjectSubmissionForm()
	return render(request, 'create-form.html', args)
"""

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
			new.credit_offered = old.credit_offered
			new.supervisor = old.supervisor
			new.pay = old.pay
			new.department = old.department
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

############ ...discover/... ################
def discover(request):
	#just added-change to get request
	if request.method == 'POST':
		category = request.POST['category']
		print category
		filter = request.POST['filter']
		projects = Project.objects.filter(category__icontains=category).order_by()
		args = {}
		args.update(csrf(request))
		args['projects'] = projects
		return render(request, 'discover.html', args)
	#end added
	category_filter = Q()
	projects_filter = Q()
	if 'category' in request.GET:
		category_filter |= Q(category=request.GET['category'])
	if 'project-search' in request.GET:	#searched from base template nav bar
		query = request.GET['project-search']
		projects = Project.objects.filter(
										Q(name__icontains=query) & 
										category_filter
		).order_by()
		return render(request, 'discover.html', {'projects':projects, 'query':query})
	return render(request, 'discover.html', {'projects':Project.objects.all()})

def project_page(request, project_url):
	project = get_object_or_404(Project, url=project_url) #finds project object in database based on url. Very cool!
	context = {'project': project}
	context.update(csrf(request))
	if request.method == 'GET':
		return render(request, 'project_page.html', context)
	profile=request.user.profile	#improve this logic: should only be able to view projects if not logged in
	if 'join-project' in request.POST and request.POST['join-project'] == 'submit': #if join project, send email to project owner for approval and add request to table for approval
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

"""Dynamic ajax search; called on every keystroke. Filters through product table in database based on query."""
def ajax_result(request):
	#print "in ajax result"
	#query = request.POST['search_text']
	if request.method == 'POST':
		#print "1"
		search_text = request.POST['search_text']
		query = search_text
		#print "2"
	else:
		search_text = ''
		query = search_text
		#print "3"
	projects = Project.objects.filter(Q(name__icontains=search_text) | Q(description__icontains=search_text))
	return render_to_response('ajax_result.html', {'projects':projects, 'query':query})
