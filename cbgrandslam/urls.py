from django.conf.urls import patterns, include, url

from django.contrib import admin
from game import urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^backend/', include(admin.site.urls)),

    #url(r'^$', 'game.views.test', name='test').


    #ADD items
    url(r'^$', 'game.views.index', name='index'),
    url(r'^game/', include('game.urls')),

    url(r'^javascript/', 'game.views.javascript'),




)
