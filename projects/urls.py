from django.conf.urls import patterns, include, url

#...projects/
urlpatterns = patterns('',
	url(r'^create/$', 'projects.views.create', name='create'),
	#url(r'^create-form/$', 'projects.views.create_form', name='create_form'),
	url(r'^create/admin-approve/$', 'projects.views.approve'),
	url(r'^discover/$', 'projects.views.discover'),
	url(ur'^projects/(?P<project_url>.*)/$', 'projects.views.project_page', name="project_page") #regex allows all chars except spaces
)
