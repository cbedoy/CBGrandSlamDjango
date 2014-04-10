from game.views import LocationCreate

__author__ = 'administrador'

from django.conf.urls import patterns, include, url
from game import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.index, name='award_list'),

    url(r'^award/list$', views.AwardList.as_view(), name='award_list'),
    url(r'^award/new$', views.AwardCreate.as_view(), name='award_new'),
    url(r'^award/edit/(?P<pk>\d+)$', views.AwardUpdate.as_view(), name='award_edit'),
    url(r'^award/delete/(?P<pk>\d+)$', views.AwardDelete.as_view(), name='award_delete'),

    url(r'^country/list$', views.CountryList.as_view(), name='country_list'),
    url(r'^country/new$', views.CountryCreate.as_view(), name='country_new'),
    url(r'^country/edit/(?P<pk>\d+)$', views.CountryUpdate.as_view(), name='country_edit'),
    url(r'^country/delete/(?P<pk>\d+)$', views.CountryDelete.as_view(), name='country_delete'),

    url(r'^game/list$', views.GameList.as_view(), name='game_list'),
    url(r'^game/new$', views.GameCreate.as_view(), name='game_new'),
    url(r'^game/edit/(?P<pk>\d+)$', views.GameUpdate.as_view(), name='game_edit'),
    url(r'^game/delete/(?P<pk>\d+)$', views.GameDelete.as_view(), name='game_delete'),

    url(r'^location/list$', views.LocationList.as_view(), name='location_list'),
    url(r'^location/new$', views.LocationCreate.as_view(), name='location_new'),
    url(r'^location/edit/(?P<pk>\d+)$', views.LocationUpdate.as_view(), name='location_edit'),
    url(r'^location/delete/(?P<pk>\d+)$', views.LocationDelete.as_view(), name='location_delete'),

    url(r'^modality/list$', views.ModalityList.as_view(), name='modality_list'),
    url(r'^modality/new$', views.ModalityCreate.as_view(), name='modality_new'),
    url(r'^modality/edit/(?P<pk>\d+)$', views.ModalityUpdate.as_view(), name='modality_edit'),
    url(r'^modality/delete/(?P<pk>\d+)$', views.ModalityDelete.as_view(), name='modality_delete'),

    url(r'^nationality/list$', views.NationalityList.as_view(), name='nationality_list'),
    url(r'^nationality/new$', views.NationalityCreate.as_view(), name='nationality_new'),
    url(r'^nationality/edit/(?P<pk>\d+)$', views.NationalityUpdate.as_view(), name='nationality_edit'),
    url(r'^nationality/delete/(?P<pk>\d+)$', views.NationalityDelete.as_view(), name='nationality_delete'),

    url(r'^player/list$', views.PlayerList.as_view(), name='player_list'),
    url(r'^player/new$', views.PlayerCreate.as_view(), name='player_new'),
    url(r'^player/edit/(?P<pk>\d+)$', views.PlayerUpdate.as_view(), name='player_edit'),
    url(r'^player/delete/(?P<pk>\d+)$', views.PlayerDelete.as_view(), name='player_delete'),

    url(r'^referee/list$', views.RefereeList.as_view(), name='referee_list'),
    url(r'^referee/new$', views.RefereeCreate.as_view(), name='referee_new'),
    url(r'^referee/edit/(?P<pk>\d+)$', views.RefereeUpdate.as_view(), name='referee_edit'),
    url(r'^referee/delete/(?P<pk>\d+)$', views.RefereeDelete.as_view(), name='referee_delete'),

    url(r'^team/list$', views.TeamList.as_view(), name='team_list'),
    url(r'^team/new$', views.TeamCreate.as_view(), name='team_new'),
    url(r'^team/edit/(?P<pk>\d+)$', views.TeamUpdate.as_view(), name='team_edit'),
    url(r'^team/delete/(?P<pk>\d+)$', views.TeamDelete.as_view(), name='team_delete'),

    url(r'^tournament/list$', views.TournamentList.as_view(), name='tournament_list'),
    url(r'^tournament/new$', views.TournamentCreate.as_view(), name='tournament_new'),
    url(r'^tournament/edit/(?P<pk>\d+)$', views.TournamentUpdate.as_view(), name='tournament_edit'),
    url(r'^tournament/delete/(?P<pk>\d+)$', views.TournamentDelete.as_view(), name='tournament_delete'),

    url(r'^trainer/list$', views.TrainerList.as_view(), name='trainer_list'),
    url(r'^trainer/new$', views.TrainerCreate.as_view(), name='trainer_new'),
    url(r'^trainer/edit/(?P<pk>\d+)$', views.TrainerUpdate.as_view(), name='trainer_edit'),
    url(r'^trainer/delete/(?P<pk>\d+)$', views.TrainerDelete.as_view(), name='trainer_delete'),


    url(r'^select$', 'game.views.query_test'),

)
