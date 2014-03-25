from django.contrib import admin
from game.models import Location, Country, Tournament
# Register your models here.

admin.site.register(Location)
admin.site.register(Country)
admin.site.register(Tournament)
