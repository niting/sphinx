from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sphinx.views.home', name='home'),
    url(r'^auth/', include('sphinx.login.urls')),
	url(r'^$', 'sphinx.views.index', name='index'),
	url(r'^questions/add', 'sphinx.views.questions_add', name='questions_add'),
	url(r'^questions/show/(?P<question_id>\d)$', 'sphinx.views.questions_show', name='questions_show'),
	#url(r'^add/post', 'sphinx.views.add_topic'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
