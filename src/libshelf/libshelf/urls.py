from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from libs.models import Library
import libs.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

library_list=ListView.as_view(model=Library)
library_detail=DetailView.as_view(model=Library)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'libshelf.views.home', name='home'),
    # url(r'^libshelf/', include('libshelf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'libs.views.list', name='list')
    url(r'^$', library_list, name='library_list'),
    url(r'^library/$', library_list, name='library_list'),
    url(r'^library/add/$', libs.views.library_add_edit, name='library_add'),
    url(r'^library/(?P<pk>[a-e\d]{24})/$', library_detail, name='library_detail'),
    url(r'^library/(?P<slug>[a-z_\-\d]+)/$', library_detail, name='library_detail'),
    url(r'^library/(?P<pk>[a-z\d]{24})/edit/$', libs.views.library_add_edit, name='library_edit'),
    url(r'^library/(?P<slug>[a-z_\-\d]+)/edit/$', libs.views.library_add_edit, name='library_edit'),
)
