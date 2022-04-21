from django.db import models

# Create your models here.

class Wind(models.Model):
    wind_speed = models.PositiveSmallIntegerField()
    creation_date = models.DateTimeField(auto_now=True)

class Rotor(models.Model):
    rotor_speed = models.PositiveSmallIntegerField()
    creation_date = models.DateTimeField(auto_now=True)

class EletricPower(models.Model):
    energy_production = models.PositiveSmallIntegerField()
    creation_date = models.DateTimeField(auto_now=True)
