__author__ = 'administrador'

from django.forms import ModelForm
from django import forms
from game.views import *
from game.models import *

class AwardForm(ModelForm):
    class Meta:
        model = Award

#lass CategoryForm(ModelForm):
#    class Meta:
#        model = Category

class CountryForm(ModelForm):
    class Meta:
        model = Country

class GameForm(ModelForm):
    class Meta:
        model = Game

class LocationForm(ModelForm):
    class Meta:
        model = Location

class ModalityForm(ModelForm):
    class Meta:
        model = Modality

class NationalityForm(ModelForm):
    class Meta:
        model = Nationality

class PlayerForm(ModelForm):
    class Meta:
        model = Player

class RefereeForm(ModelForm):
    class Meta:
        model = Referee

class TeamForm(ModelForm):
    class Meta:
        model = Team

class TrainerForm(ModelForm):
    class Meta:
        model = Trainer




