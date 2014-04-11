from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.db import connection


def index(request):
    data = {'nombre': 'Carlos Alfredo Cervantes Bedoy', 'materia': 'Taller II', 'maestro': 'Guadalupe',
            'proyecto': 'CBGrandSlam', 'carrera': 'Tecnologias de informacion', 'grado': '8', 'grupo': 'B',
            'soporte': 'Soporte a Oracle, MySQL, SQLite', 'lenguaje': 'Python 2.7',
            'framework': 'Django, JQuery, Javascript, JQueryMobile', 'github':'https://github.com/cbedoy/CBGrandSlamDjango'}

    return render_to_response('index.html', data)

#LOCATIONS --------------------------------------------------------------------------


class LocationList(ListView):
    model = Location


class LocationCreate(CreateView):
    model = Location
    success_url = reverse_lazy('location_list')


class LocationUpdate(UpdateView):
    model = Location
    success_url = reverse_lazy('location_list')


class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('location_list')

#COUNTRY --------------------------------------------------


class CountryList(ListView):
    model = Country


class CountryCreate(CreateView):
    model = Country
    success_url = reverse_lazy('country_list')


class CountryUpdate(UpdateView):
    model = Country
    success_url = reverse_lazy('country_list')


class CountryDelete(DeleteView):
    model = Country
    success_url = reverse_lazy('country_list')

#TOURNAMENT -----------------------------------------------------


class TournamentList(ListView):
    model = Tournament


class TournamentCreate(CreateView):
    model = Tournament
    success_url = reverse_lazy('tournament_list')


class TournamentUpdate(UpdateView):
    model = Tournament
    success_url = reverse_lazy('tournament_list')


class TournamentDelete(DeleteView):
    model = Tournament
    success_url = reverse_lazy('tournament_list')


#REFEREE -----------------------------------------------------


class RefereeList(ListView):
    model = Referee


class RefereeCreate(CreateView):
    model = Referee
    success_url = reverse_lazy('referee_list')


class RefereeUpdate(UpdateView):
    model = Referee
    success_url = reverse_lazy('referee_list')


class RefereeDelete(DeleteView):
    model = Referee
    success_url = reverse_lazy('referee_list')



#TRAINER -----------------------------------------------------

class TrainerList(ListView):
    model = Trainer


class TrainerCreate(CreateView):
    model = Trainer
    success_url = reverse_lazy('trainer_list')


class TrainerUpdate(UpdateView):
    model = Trainer
    success_url = reverse_lazy('trainer_list')


class TrainerDelete(DeleteView):
    model = Trainer
    success_url = reverse_lazy('trainer_list')



#NATIONALITY -----------------------------------------------------

class NationalityList(ListView):
    model = Nationality


class NationalityCreate(CreateView):
    model = Nationality
    success_url = reverse_lazy('nationality_list')


class NationalityUpdate(UpdateView):
    model = Nationality
    success_url = reverse_lazy('nationality_list')


class NationalityDelete(DeleteView):
    model = Nationality
    success_url = reverse_lazy('nationality_list')


#Teams --------------------------

class TeamList(ListView):
    model = Team


class TeamCreate(CreateView):
    model = Team
    success_url = reverse_lazy('team_list')


class TeamUpdate(UpdateView):
    model = Team
    success_url = reverse_lazy('team_list')


class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('team_list')

##PLAYER -------------------------

class PlayerList(ListView):
    model = Player


class PlayerCreate(CreateView):
    model = Player
    success_url = reverse_lazy('player_list')


class PlayerUpdate(UpdateView):
    model = Player
    success_url = reverse_lazy('player_list')


class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player_list')


##AWARD -------------------------

class AwardList(ListView):
    model = Award


class AwardCreate(CreateView):
    model = Award
    success_url = reverse_lazy('award_list')


class AwardUpdate(UpdateView):
    model = Award
    success_url = reverse_lazy('award_list')


class AwardDelete(DeleteView):
    model = Award
    success_url = reverse_lazy('award_list')


##GAME -------------------------

class GameList(ListView):
    model = Game


class GameCreate(CreateView):
    model = Game
    success_url = reverse_lazy('game_list')


class GameUpdate(UpdateView):
    model = Game
    success_url = reverse_lazy('game_list')


class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('game_list')




def query_test(request):
    cursor = connection.cursor()
    cursor.execute(
        'select name as name, (select name from game_country where id=country_id)  as location from game_location')
    results = cursor.fetchall()
    return render_to_response('hard_queries/four.html', {"results":results})