__author__ = 'administrador'

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^award/', 'game.views.newAward', name='newAward'),
    #url(r'^category/', 'game.views.addCategory'),
    url(r'^country/', 'game.views.newCountry', name='newCountry'),
    url(r'^game/', 'game.views.newGame', name='new'),
    url(r'^location/', 'game.views.newLocation', name='newLocation'),
    url(r'^modality/', 'game.views.newModality', name='newModality'),
    url(r'^nationality/', 'game.views.newNationality', name='newNationality'),
    url(r'^player/', 'game.views.newPlayer', name='newPlayer'),
    url(r'^referee/', 'game.views.newReferee', name='newReferee'),
    url(r'^team/', 'game.views.newTeam', name='newTeam'),
    url(r'^trainer/', 'game.views.newTrainer', name='newTrainer'),



)
