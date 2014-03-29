__author__ = 'administrador'

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    url(r'^', 'game.views.index'),
    url(r'^award/', 'game.views.newAward'),
    #url(r'^category/', 'game.views.addCategory'),
    url(r'^country/', 'game.views.newCountry'),
    url(r'^game/', 'game.views.newGame'),
    url(r'^location/', 'game.views.newLocation'),
    url(r'^modality/', 'game.views.newModality'),
    url(r'^nationality/', 'game.views.newNationality'),
    url(r'^player/', 'game.views.newPlayer'),
    url(r'^referee/', 'game.views.newReferee'),
    url(r'^team/', 'game.views.newTeam'),
    url(r'^trainer/', 'game.views.newTrainer'),



)
