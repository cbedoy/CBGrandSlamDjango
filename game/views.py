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

def newCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CategoryForm()
    name = "New category"
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

