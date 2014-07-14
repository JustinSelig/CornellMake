from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^create/$', 'projects.views.create', name='create_product'),
)