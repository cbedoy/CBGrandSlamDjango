from django.db import models
from django.core.urlresolvers import reverse

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

    def get_absolute_url(self):
        return reverse('location_edit', kwargs={'pk': self.pk})


class Tournament(models.Model):
    year_l = (
        (2010, '2010'),
        (2011, '2011'),
        (2012, '2012'),
        (2013, '2013'),
        (2014, '2014'),
        (2015, '2015'),
        (2016, '2016'),
        (2017, '2017'),
        (2018, '2018'),
        (2019, '2019'),
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
    )
    name = models.CharField(max_length=45)
    year = models.IntegerField(choices=year_l)
    description = models.TextField(max_length=100)
    country = models.ForeignKey(Country)

    def __unicode__(self):
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

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName


class Trainer(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    initialDate = models.DateField()
    lastDate = models.DateField()
    unicode(initialDate)
    unicode(lastDate)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName


class Nationality(models.Model):
    name = models.CharField(max_length=45)
    link = models.CharField(max_length=150)
    abreviature = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name + '-' + self.abreviature


class Modality(models.Model):
    name_l = (
        ('SINGLE-M', 'SINGLE-M'),
        ('TEAM-M', 'TEAM-M'),
        ('SINGLE-F', 'SINGLE-F'),
        ('TEAM-F', 'TEAM-F'),
        ('MIX', 'MIX'),
    )
    name = models.CharField(max_length=10, choices=name_l)
    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=45)
    modality = models.ForeignKey(Modality)
    facebook = models.CharField(max_length=45)
    twitter = models.CharField(max_length=45)
    def __unicode__(self):
        return self.name + ' => ' + self.modality.name

class Player(models.Model):
    sex_l = (
        ('F', 'Female'),
        ('M', 'Masculine'),
    )
    age_l = (
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
    )
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField(choices=age_l)
    sex = models.CharField(max_length=10, choices=sex_l)
    height = models.FloatField()
    weight = models.FloatField()
    games = models.IntegerField()
    amount = models.FloatField()
    web = models.CharField(max_length=45, null=True)
    facebook = models.CharField(max_length=45, null=True)
    telephone = models.CharField(max_length=45, null=True)

    nationality = models.ForeignKey(Nationality)
    trainer = models.ForeignKey(Trainer)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName

class Award(models.Model):
    name = models.CharField(max_length=45)
    amount = models.FloatField()
    description = models.TextField(max_length=100)
    tournament = models.ForeignKey(Tournament)
    player = models.ForeignKey(Player)
    trainer = models.ForeignKey(Trainer)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    referee = models.ForeignKey(Referee)
    teamA = models.ForeignKey(Team, related_name='idA')
    teamB = models.ForeignKey(Team, related_name='idB')
    tournament = models.ForeignKey(Tournament)
    def __unicode__(self):
        return self.name




