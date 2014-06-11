from django.conf.urls import patterns, include, url
from nails.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'nails.views.index'),
     url(r'^index/$', 'nails.views.index', name='index'),
     url(r'^about/$', 'nails.views.about', name='about'),
     url(r'^product/$', 'nails.views.product', name='product'),
     url(r'^contact/$', 'nails.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
