from django.conf.urls import patterns, include, url

#...projects/
urlpatterns = patterns('',
	url(r'^create/$', 'projects.views.create', name='create'),
#	url(r'^create_success/$', 'projects.views.create_success', name='create_success'),
	url(r'^admin-approve/$', 'projects.views.approve'),
	url(r'^(?P<project_url>\w+)/$', 'projects.views.project_page', name="project_page")
)