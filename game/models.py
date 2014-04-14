from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=45)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name


class Nationality(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name


class Referee(models.Model):
    time_l = (
        ('HT', 'Hall Time'),
        ('AT', 'All Time'),
    )
    firstName = models.CharField('First name', max_length=45)
    lastName = models.CharField('Last name', max_length=45)
    nationality = models.ForeignKey(Nationality)
    age_l = (
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
        (32, '32'),
        (33, '33'),
        (34, '34'),
        (35, '35'),
        (36, '36'),
        (37, '37'),
        (38, '38'),
        (39, '39'),
        (40, '40'),
    )
    age = models.IntegerField(choices=age_l)
    time = models.CharField(max_length=45, choices=time_l)
    email = models.CharField(max_length=45, null=True)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName


class Trainer(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    nationality = models.ForeignKey(Nationality)
    age_l = (
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
        (32, '32'),
        (33, '33'),
        (34, '34'),
        (35, '35'),
        (36, '36'),
        (37, '37'),
        (38, '38'),
        (39, '39'),
        (40, '40'),
    )
    age = models.IntegerField(choices=age_l)
    email = models.CharField(max_length=45, null=True)
    initialDate = models.DateField('Initial date')
    lastDate = models.DateField('Last date')
    unicode(initialDate)
    unicode(lastDate)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName


class Team(models.Model):
    modality_l = (
        ('SINGLE-M', 'SINGLE-MALE'),
        ('TEAM-M', 'TEAM-MALE'),
        ('SINGLE-F', 'SINGLE-FEMALE'),
        ('TEAM-F', 'TEAM-FEMALE'),
        ('MIXED', 'MIXED'),
    )
    name = models.CharField(max_length=45, unique=True)
    facebook = models.CharField(max_length=45, null=True)
    twitter = models.CharField(max_length=45, null=True)
    modality = models.CharField(choices=modality_l, max_length=10)
    unicode(name)

    def __unicode__(self):
        return self.name + ' :: ' + self.modality


class Player(models.Model):
    sex_l = (
        ('F', 'Female'),
        ('M', 'Male'),
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
    firstName = models.CharField('First name', max_length=45)
    lastName = models.CharField('Last name', max_length=45)
    age = models.IntegerField(choices=age_l)
    sex = models.CharField(max_length=10, choices=sex_l)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    web = models.CharField(max_length=45, null=True)
    facebook = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null=True)
    nationality = models.ForeignKey(Nationality)
    trainer = models.ForeignKey(Trainer)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self.firstName + ' ' + self.lastName


class Tournament(models.Model):
    name = models.CharField(max_length=45)
    year_l = (
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
        (2023, '2024'),
        (2023, '2025'),

    )
    year = models.IntegerField(choices=year_l)

    def __unicode__(self):
        return self.name + ' :: ' + str(self.year)


class Game(models.Model):
    referee = models.ForeignKey(Referee)
    teamA = models.ForeignKey(Team, related_name='idA')
    teamB = models.ForeignKey(Team, related_name='idB')
    tournament = models.ForeignKey(Tournament)
    location = models.ForeignKey(Location)
    date = models.DateField()

    def __unicode__(self):
        return self.teamA.name + ' VS ' + self.teamB.name


class Award(models.Model):
    name = models.CharField(max_length=45)
    amount = models.FloatField()
    description = models.CharField(max_length=45)
    player = models.ForeignKey(Player)

    def __unicode__(self):
        return self.name





