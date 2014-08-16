from django.conf.urls import patterns, include, url

#...projects/
urlpatterns = patterns('',
	url(r'^create/$', 'projects.views.create', name='create'),
	url(r'^admin-approve/$', 'projects.views.approve'),
	url(ur'^(?P<project_url>.*)/$', 'projects.views.project_page', name="project_page") #regex allows all chars except spaces
)