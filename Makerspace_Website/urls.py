from django.conf.urls import patterns, include, url
from views import *
from events.views import home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Makerspace_Website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^home/$', home),
	url(r'^about/$', about),
	url(r'^media/$', media),
	url(r'^create/$', create),
)
