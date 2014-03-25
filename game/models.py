from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=45)
    longitud = models.FloatField()
    latitud = models.FloatField()
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=45)
    year = models.DateField('2007')
    name = models.TextField(max_length=300)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name


class Referee(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    time = models.CharField(max_length=45)

    def __unicode__(self):
        return self.firstName+self.lastName

class Trainer(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    initialDate = models.DateField()
    lastDate = models.DateField()

    def __unicode__(self):
        return self.firstName + self.lastDate

class Game(models.Model):
    modality = models.CharField(max_length=45)

    def __unicode__(self):
        return self.modality

class Player (models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    wins = models.IntegerField()
    losts = models.IntegerField()

    def __unicode__(self):
        return self.firstName+self.lastName

class Nationality(models.Model):
    name = models.CharField(max_length=45)
    abreviature = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name+'-'+self.abreviature

class Award(models.Model):
    name = models.CharField(max_length=45)
    amount = models.FloatField()
    description = models.TextField(max_length=100)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=45)
    abreviature = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name+'-'+self.abreviature


