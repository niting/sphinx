from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sphinx.views.home', name='home'),
    # url(r'^sphinx/', include('sphinx.foo.urls')),
	url(r'^$', 'sphinx.views.index', name='index'),
	url(r'^add/question', 'sphinx.views.add_question', name='add_question'),
	url(r'^add/post', 'sphinx.views.add_topic'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
