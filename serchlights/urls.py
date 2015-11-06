from django.conf.urls import patterns, include, url

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'subscribe.views.alert'),
    url(r'^subscribe/$', 'subscribe.views.subscribe'),
    url(r'^subscribe/success/$', 'subscribe.views.success'),
    #url(r'^subscribe/error/$', 'subscribe.views.error'),
    
)
