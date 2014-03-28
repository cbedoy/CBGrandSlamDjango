from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *
from .forms import *


def awards(request):
    data = Award.objects.all()
    return render_to_response('locations.html', dict(awards=data), context_instance=RequestContext(request))

def countries(request):
    data = Country.objects.all()
    return render_to_response('locations.html', dict(countries=data), context_instance=RequestContext(request))


def games(request):
    data = Game.objects.all()
    return render_to_response('locations.html', dict(games=data), context_instance=RequestContext(request))


def locations(request):
    data = Location.objects.all()
    return render_to_response('locations.html', dict(locations=data), context_instance=RequestContext(request))


def nationalities(request):
    data = Nationality.objects.all()
    return render_to_response('locations.html', dict(nationalities=data), context_instance=RequestContext(request))


def players(request):
    data = Player.objects.all()
    return render_to_response('locations.html', dict(players=data), context_instance=RequestContext(request))


def referees(request):
    data = Referee.objects.all()
    return render_to_response('locations.html', dict(referees=data), context_instance=RequestContext(request))


def teams(request):
    doubleTeams = DoubleTeam.objects.all()
    singleTeams = SingleTeam.objects.all()
    data = [doubleTeams, singleTeams]
    return render_to_response('locations.html', dict(teams=data), context_instance=RequestContext(request))


def trainers(request):
    data = Trainer.objects.all()
    return render_to_response('locations.html', dict(trainers=data))


def index(request):
    data = {'nombre': 'Carlos Alfredo Cervantes Bedoy', 'materia': 'Taller II', 'maestro': 'Guadalupe',
            'proyecto': 'CBGrandSlam', 'carrera': 'Tecnologias de informacion', 'grado': '8', 'grupo': 'B',
            'soporte': 'Soporte a Oracle, MySQL, SQLite', 'lenguaje': 'Python 2.7',
            'framework': 'Django, JQuery, Javascript, JQueryMobile', 'github':'https://github.com/cbedoy/CBGrandSlamDjango'}

    return render_to_response('index.html', data)

def test(request):
    data = Country.objects.all()
    return render_to_response('test.html', {"data": data},  context_instance=RequestContext(request))