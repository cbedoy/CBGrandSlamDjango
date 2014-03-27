from django.shortcuts import render_to_response

from game.models import Location

def allLocations(request):
    data = Location.objects.all()
    return render_to_response('locations.html', {'articulos' : data})