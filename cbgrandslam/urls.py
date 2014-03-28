from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^backend/', include(admin.site.urls)),

    url(r'^$', 'game.views.test', name='test')

)
