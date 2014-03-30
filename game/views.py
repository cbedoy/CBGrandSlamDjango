from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *
from .forms import *


def awards(request):
    data = Award.objects.raw("select * from game_award")
    return render_to_response('reports/getAwards.html', {"form": data}, context_instance=RequestContext(request))


def countries(request):
    data = Award.objects.raw("select * from game_country")
    return render_to_response('reports/getCountries.html', {"form": data}, context_instance=RequestContext(request))


def games(request):
    data = Award.objects.raw("select * from game_game")
    return render_to_response('reports/getGames.html', {"form": data}, context_instance=RequestContext(request))


def locations(request):
    data = Award.objects.raw("select * from game_location")
    return render_to_response('reports/getLocations.html', {"form": data}, context_instance=RequestContext(request))


def nationalities(request):
    data = Award.objects.raw("select * from game_nationality")
    return render_to_response('reports/getNationalities.html', {"form": data}, context_instance=RequestContext(request))


def players(request):
    data = Award.objects.raw("select * from game_player")
    return render_to_response('reports/getPlayers.html', {"form": data}, context_instance=RequestContext(request))


def referees(request):
    data = Award.objects.raw("select * from game_referee")
    return render_to_response('reports/getReferees.html', {"form": data}, context_instance=RequestContext(request))


def teams(request):
    data = Location.objects.raw("select * from game_teams")
    return render_to_response('reports/getTeams.html', dict(teams=data), context_instance=RequestContext(request))


def trainers(request):
    data = Award.objects.raw("select * from game_trainer")
    return render_to_response('reports/getTrainers.html', {"form": data}, context_instance=RequestContext(request))


def modalities(request):
    data = Award.objects.raw("select * from game_modality")
    return render_to_response('reports/getModalities.html', {"form": data}, context_instance=RequestContext(request))


def index(request):
    data = {'nombre': 'Carlos Alfredo Cervantes Bedoy', 'materia': 'Taller II', 'maestro': 'Guadalupe',
            'proyecto': 'CBGrandSlam', 'carrera': 'Tecnologias de informacion', 'grado': '8', 'grupo': 'B',
            'soporte': 'Soporte a Oracle, MySQL, SQLite', 'lenguaje': 'Python 2.7',
            'framework': 'Django, JQuery, Javascript, JQueryMobile', 'github':'https://github.com/cbedoy/CBGrandSlamDjango'}

    return render_to_response('index.html', data)


def test(request):
    data = Country.objects.all()
    return render_to_response('test.html', {"data": data},  context_instance=RequestContext(request))


def javascript(request):
    product1 = ['pendientes',  'pendiente pequeno',  '10 euros' ]
    product2 = { 'name': 'pendientes' , 'description' : 'Pendientes aro bronce', 'price' : '14.6 euro' }
    return render_to_response('javascript.html', {'product1' : product1,'product2' : product2,})
#
#
# MODEL FORM
#


def newAward(request):
    if request.method == 'POST':
        form = AwardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AwardForm()

    name = "New award"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))



def newCountry(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CountryForm()
    name = "New country"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GameForm()
    name = "New game"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newLocation(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LocationForm()
    name = "New location"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newModality(request):
    if request.method == 'POST':
        form = ModalityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ModalityForm()
    name = "New modality"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newNationality(request):
    if request.method == 'POST':
        form = NationalityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = NationalityForm()
    name = "New nationality"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newPlayer(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PlayerForm()
    name = "New player"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newReferee(request):
    if request.method == 'POST':
        form = RefereeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RefereeForm()
    name = "New referee"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newTeam(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TeamForm()
    name = "New team"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))


def newTrainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TrainerForm()
    name = "New trainer"
    proj = "CBGranSlam"
    return render_to_response('new_item.html', {'form': form, "name":name, "app":proj}, context_instance=RequestContext(request))

