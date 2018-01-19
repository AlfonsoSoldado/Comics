#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.search'),
    url(r'^populate', 'main.views.populateDB'),
    url(r'^use-populate', 'main.views.index'),
    url(r'^populate', 'main.views.populateDB'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

