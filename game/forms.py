__author__ = 'administrador'

from django.forms import ModelForm
from django import forms
from game.views import *

class LocationsForm(ModelForm):
    class Meta:
        model = Location


