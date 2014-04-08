from game.views import LocationCreate

__author__ = 'administrador'

from django.conf.urls import patterns, include, url
from game import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    url(r'^list$', views.LocationList.as_view(), name='location_list'),
    url(r'^new$', views.LocationCreate.as_view(), name='location_new'),
    url(r'^edit/(?P<pk>\d+)$', views.LocationUpdate.as_view(), name='location_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.LocationDelete.as_view(), name='location_delete'),


)
