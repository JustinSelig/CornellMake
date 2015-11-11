from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
from media.views import media
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Makerspace_Website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', home),
	url(r'^about/$', about),
	url(r'^media/$', media),
	#url(r'^create/$', create),
#	(r'^projects/', include('projects.urls')),
	(r'', include('projects.urls')),
	(r'^accounts/', include('accounts.urls')),
)
