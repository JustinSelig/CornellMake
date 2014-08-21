from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
#from userprofile.views import force_profile
#from userprofile.models import UserProfile
#from userprofile.forms import UserProfileForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse

def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		username = request.POST.get('username')
		if form.is_valid():
			print "valid form"
			form.save()
#			force_profile(request, username)
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
				args['error'] = 'An account with that email may already exist. Please use a different one.'
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
#			user = request.user
#			form = UserProfileForm(instance=user.profile)
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


#def delete_user(request):
#	pass