__author__ = 'administrador'

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    url(r'^Award/', 'game.views.addAward'),
    url(r'^Category/', 'game.views.addCategory'),
    url(r'^Country/', 'game.views.addCountry'),
    url(r'^Game/', 'game.views.addGame'),
    url(r'^Location/', 'game.views.addLocation'),
    url(r'^Modality/', 'game.views.addModality'),
    url(r'^Nationality/', 'game.views.addNationality'),
    url(r'^Player/', 'game.views.addPlayer'),
    url(r'^Referee/', 'game.views.addReferee'),
    url(r'^Team/', 'game.views.addTeam'),
    url(r'^Trainer/', 'game.views.addTrainer'),



)
