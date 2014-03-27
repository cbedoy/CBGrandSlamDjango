from django.shortcuts import render_to_response

from .models import *

def getAwards(request):
    data = Award.objects.all()
    return render_to_response('locations.html', dict(awards=data))

def getCategories(request):
    data = Category.objects.all()
    return render_to_response('locations.html', dict(categories=data))

def getCountries(request):
    data = Country.objects.all()
    return render_to_response('locations.html', dict(countries=data))

def getGames(request):
    data = Game.objects.all()
    return render_to_response('locations.html', dict(games=data))

def getLocations(request):
    data = Location.objects.all()
    return render_to_response('locations.html', dict(locations=data))

def getModalities(request):
    data = Modality.objects.all()
    return render_to_response('locations.html', dict(modalities=data))

def getNationalities(request):
    data = Nationality.objects.all()
    return render_to_response('locations.html', dict(nationalities=data))

def getPlayers(request):
    data = Player.objects.all()
    return render_to_response('locations.html', dict(players=data))

def getReferees(request):
    data = Referee.objects.all()
    return render_to_response('locations.html', dict(referees=data))

def getTeams(request):
    doubleTeams = DoubleTeam.objects.all()
    singleTeams = SingleTeam.objects.all()
    data = [doubleTeams, singleTeams]
    return render_to_response('locations.html', dict(teams=data))

def getTrainers(request):
    data = Trainer.objects.all()
    return render_to_response('locations.html', dict(trainers=data))

