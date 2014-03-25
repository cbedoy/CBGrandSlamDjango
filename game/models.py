from django.db import models

# Create your models here.

class Country(models.Model):
    name    = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    name    = models.CharField(max_length=45)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

class Tournament(models.Model):
    name    = models.CharField(max_length=45)
    year    = models.DateField('2007')
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name
