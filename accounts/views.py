from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
#from userprofile.views import force_profile
from models import UserProfile
from forms import UserProfileForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404

############ USER REGISTRATION AND LOGIN ####################

def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		username = request.POST.get('username') #set username to email?? how to make username not a field??
		if form.is_valid():
			print "valid form"
			form.save()
			make_user_profile(request, username)
			args = {'success':'Your account has been created. Please use the information you provided to log in below.'}
			return render(request, 'login.html', args)
		else:
			print "invalid form"
			args = {}
			args.update(csrf(request))
			args['form'] = MyRegistrationForm()
			if request.POST.get('password1') != request.POST.get('password2'):
				args['error'] = 'Passwords do not match'
			else:
				args['error'] = 'An account with that username may already exist. Please use a different one.'
			return render(request, 'register.html', args)
	args = {}
	args.update(csrf(request))
	args['form'] = MyRegistrationForm()
	return render(request, 'register.html', args)

def login(request):
	if request.method == 'POST':
		#username = request.POST.get('username', ' ')
		password = request.POST.get('password', ' ')
		email = request.POST.get('email', ' ')
		#user = auth.authenticate(username=username, password=password)
		user = auth.authenticate(password=password, email=email, username=email)
		if user is not None:
			auth.login(request, user)
#			form = UserProfileForm(instance=request.user.profile)
#			context = {}
#			context.update(csrf(request))
#			context['form'] = form
			return HttpResponseRedirect('/')
		else:
			context = {}
			context.update(csrf(request))
			context['invalid']= 'The username and password combination entered do match any known member\'s.'
			return render(request, 'login.html', context)
	context = {}
	context.update(csrf(request))
	return render(request, 'login.html', context)

def logout(request):
	auth.logout(request)
	return render(request, 'login.html')

############### USER PROFILE #####################

"""Called during user registration"""
def make_user_profile(request, username):
	user = User.objects.get(username=username)
	profile = user.profile #triggers django to create profile and populate it if not extant
	form = UserProfileForm(instance=profile)
	prof = UserProfile.objects.get(user_id=user.id)
	prof.username = username
	prof.save()
	args = {}
	args.update(csrf(request))
	args['form'] = form #I don't think 'form' is necessary, or the return statement
	return args

"""Renders profile that is only available to loggedin user. It is editable. 
All changes made here are published in the public profile"""
@login_required
def private_user_profile(request):
	profile = request.user.profile
	args = {'profile':profile}
	args['member_requests'] = UserProfile.objects.get(user_id=request.user.id).member_requests.all()
	if request.method == 'POST':
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		major = request.POST.get('major')
		school = request.POST.get('school')
		profile.email = email
		profile.phone = phone
		profile.major = major
		profile.school = school
		profile.save()
		args['profile_change'] = True
		return render(request, 'private_user_profile.html', args)
	#show join requests
	return render(request, 'private_user_profile.html', args)

"""Renders public user profile page"""
def public_user_profile(request, username):
	try: profile = UserProfile.objects.get(user__username=username) #use '__' instead of '.' since invocation, not expression
	except: raise Http404 #handle this!!!
	#username cannot be unicode? would representation in browser be same as in server? (ex. %3B)
#	profile = request.user.profile #triggers django to create profile and populate it if not extant
#	form = UserProfileForm(instance=profile)
	args = {'profile': profile}
	return render(request, 'public_user_profile.html', args)

def delete_user(request):
	pass


###################### 	PASSWORD RESET ######################
"""
def reset(request):
	return password_reset(request, template_name='password_reset_form.html',
	  email_template_name='password_reset_email.html',
	  subject_template_name='reset_subject.txt',
	  post_reset_redirect=reverse('password_reset_done'))

def reset_done(request):
	return password_reset_done(request, template_name='password_reset_done.html')


def reset_confirm(request, uidb64=None, token=None):
	return password_reset_confirm(request, template_name='password_reset_confirm.html',
	  uidb64=uidb64, token=token, post_reset_redirect=reverse('password_reset_complete'))

def reset_complete(request):
	return password_reset_complete(request, template_name='password_reset_complete.html')
"""
