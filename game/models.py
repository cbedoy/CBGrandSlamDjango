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
    year = models.DateField()
    description = models.TextField(max_length=100)
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

class Nationality(models.Model):
    name = models.CharField(max_length=45)
    abreviature = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name+'-'+self.abreviature

class Player(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    wins = models.IntegerField()
    losts = models.IntegerField()
    nationality = models.ForeignKey(Nationality)
    trainer = models.ForeignKey(Trainer)

    def __unicode__(self):
        return self.firstName+self.lastName

class Modality(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=45)
    trainer = models.ForeignKey(Trainer)
    referee = models.ForeignKey(Referee)
    player = models.ForeignKey(Player)
    tournament = models.ForeignKey(Tournament)

    def __unicode__(self):
        return self.name





class Award(models.Model):
    name = models.CharField(max_length=45)
    amount = models.FloatField()
    description = models.TextField(max_length=100)
    tournament = models.ForeignKey(Tournament)
    player = models.ForeignKey(Player)
    trainer = models.ForeignKey(Trainer)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=45)
    abreviature = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name+'-'+self.abreviature


class Team(models.Model):
    name = models.CharField(max_length=45)
    playerA = models.ForeignKey(Player)
    playerB = models.ForeignKey(Player)

    def __unicode__(self):
        return self.name

class Single(models.Model):
    name = models.CharField(max_length=45)
    player = models.ForeignKey(Player)

    def __unicode__(self):
        return self.name


