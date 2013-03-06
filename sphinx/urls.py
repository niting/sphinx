from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sphinx.views.home', name='home'),
    url(r'^auth/', include('sphinx.login.urls')),
	url(r'^profile/','sphinx.views.profile', name='profile'),
	url(r'^$', 'sphinx.views.index', name='index'),
	url(r'^questions/add', 'sphinx.views.add_question', name='questions_add'),
	#url(r'^add/post', 'sphinx.views.add_topic'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
