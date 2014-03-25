from django.db import models

# Create your models here.

class pais(models.Model):
    nombre = models.CharField(max_length=45)

class lugar(models.Model):
    nombre = models.CharField(max_length=45)
    idPais = models.ForeignKey(pais)


