from django.conf.urls import patterns, url
#from views import reset, reset_done, reset_confirm, reset_complete

# ...acccounts/...
urlpatterns = patterns('',
	url(r'^login/$', 'accounts.views.login', name='login'),
	url(r'^logout/$', 'accounts.views.logout', name='logout'),
	url(r'^register/$', 'accounts.views.register', name='register'),
#	url(r'^password/reset/$', reset),
#    url(r'^password/reset/done/$', reset_done, name="password_reset_done"),
#    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', reset_confirm, name="password_reset_confirm"),
#    url(r'^password/done/$', reset_complete, name="password_reset_complete"),

	#public and private user profile
	url(r'^user/profile/$', 'accounts.views.private_user_profile', name="private_user_profile"),	#this needs to come before next url!
	url(ur'^user/(?P<username>.*)/$', 'accounts.views.public_user_profile', name="public_user_profile"),
#	url(ur'^user/(?P<username>.*)/edit/$', 'accounts.views.user_profile_edit', name="user_profile_edit"),
)