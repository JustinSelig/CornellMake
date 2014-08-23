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

############ USER REGISTRATION AND LOGIN ####################

def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		username = request.POST.get('username')
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
		username = request.POST.get('username', ' ')
		password = request.POST.get('password', ' ')
		user = auth.authenticate(username=username, password=password)
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
def personal_user_profile(request):
	pass

"""Renders public user profile page"""
def public_user_profile(request, username):
	try: u = UserProfile.objects.get(user__username=username) #use '__' instead of '.' since invocation, not expression
	except: u = request.user.profile #gets or creates profile if not extant
	#username cannot be unicode? would representation in browser be same as in server? (ex. %3B)
#	profile = request.user.profile #triggers django to create profile and populate it if not extant
#	form = UserProfileForm(instance=profile)
	args = {}
#	args.update(csrf(request))
#	args['form'] = form
	args['this_profile'] = u
	args['this_user'] = u.user
	return render(request, 'user_profile.html', args)

"""May not be necessary now with personal_user_profile"""
def user_profile_edit(request, username):
	pass

def delete_user(request):
	pass


###################### 	PASSWORD RESET ######################

def reset(request):
	pass

def reset_done(request):
	pass

def reset_confirm(request, uidb64=None, token=None):
	pass

def reset_complete(request):
	pass