from django.shortcuts import render_to_response

from .models import *


def awards(request):
    data = Award.objects.all()
    return render_to_response('locations.html', dict(awards=data))


def categories(request):
    data = Category.objects.all()
    return render_to_response('locations.html', dict(categories=data))


def countries(request):
    data = Country.objects.all()
    return render_to_response('locations.html', dict(countries=data))


def games(request):
    data = Game.objects.all()
    return render_to_response('locations.html', dict(games=data))


def locations(request):
    data = Location.objects.all()
    return render_to_response('locations.html', dict(locations=data))


def modalities(request):
    data = Modality.objects.all()
    return render_to_response('locations.html', dict(modalities=data))


def nationalities(request):
    data = Nationality.objects.all()
    return render_to_response('locations.html', dict(nationalities=data))


def players(request):
    data = Player.objects.all()
    return render_to_response('locations.html', dict(players=data))


def referees(request):
    data = Referee.objects.all()
    return render_to_response('locations.html', dict(referees=data))


def teams(request):
    doubleTeams = DoubleTeam.objects.all()
    singleTeams = SingleTeam.objects.all()
    data = [doubleTeams, singleTeams]
    return render_to_response('locations.html', dict(teams=data))


def trainers(request):
    data = Trainer.objects.all()
    return render_to_response('locations.html', dict(trainers=data))

