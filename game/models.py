from django.db import models
from datetime import *

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=45)
    longitud = models.FloatField()
    latitud = models.FloatField()
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=45)
    year = models.DateField()
    description = models.TextField(max_length=100)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


class Referee(models.Model):
    time_l = (
        ('QT', 'Quart time'),
        ('MT', 'Medium time'),
        ('AT', 'All time'),
    )
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    time = models.CharField(max_length=45, choices=time_l)

    def __str__(self):
        return self.firstName+' '+self.lastName

class Trainer(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    initialDate = models.DateField()
    lastDate = models.DateField()

    def __str__(self):
        return self.firstName+' '+self.lastDate

    def __unicode__(self):
        return unicode(self.initialDate)

class Nationality(models.Model):
    name = models.CharField(max_length=45)
    link = models.CharField(max_length=150)
    abreviature = models.CharField(max_length=3)

    def __str__(self):
        return self.name+'-'+self.abreviature

class Player(models.Model):
    sex_l = (
        ('F', 'Female'),
        ('M', 'Masculine'),
    )
    age_l = (
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
    )
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField(choices=age_l)
    sex = models.CharField(max_length=10, choices=sex_l)
    height = models.FloatField()
    weight = models.FloatField()
    games = models.IntegerField()
    wins = models.IntegerField()
    lost = models.IntegerField()
    web = models.CharField(max_length=45, null=True)
    facebook = models.CharField(max_length=45, null=True)
    telephone = models.CharField(max_length=45, null=True)

    nationality = models.ForeignKey(Nationality)
    trainer = models.ForeignKey(Trainer)

    def __str__(self):
        return self.firstName+' '+self.lastName

class Modality(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=45)
    trainer = models.ForeignKey(Trainer)
    referee = models.ForeignKey(Referee)
    player = models.ForeignKey(Player)
    tournament = models.ForeignKey(Tournament)

    def __str__(self):
        return self.name





class Award(models.Model):
    name = models.CharField(max_length=45)
    amount = models.FloatField()
    description = models.TextField(max_length=100)
    tournament = models.ForeignKey(Tournament)
    player = models.ForeignKey(Player)
    trainer = models.ForeignKey(Trainer)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=45)
    abreviature = models.CharField(max_length=3)

    def __str__(self):
        return self.name+'-'+self.abreviature


class DoubleTeam(models.Model):
    name = models.CharField(max_length=45)
    facebook = models.CharField(max_length=45, null=True)
    twitter = models.CharField(max_length=45, null=True)
    playerA = models.ForeignKey(Player, related_name='idA')
    playerB = models.ForeignKey(Player, related_name='idB')


    def __str__(self):
        return self.name

class SingleTeam(models.Model):
    name = models.CharField(max_length=45)
    facebook = models.CharField(max_length=45, null=True)
    twitter = models.CharField(max_length=45, null=True)
    player = models.ForeignKey(Player)

    def __str__(self):
        return self.name




