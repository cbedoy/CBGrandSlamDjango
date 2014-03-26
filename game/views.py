from django.shortcuts import render_to_response

from game.models import Location

def home(request):
    data = Location.objects.all()
    return render_to_response('index.html', {'articulos' : data})