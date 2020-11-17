from django.db import models
from .Airplane import *

class Tickets(models.Model):
    flightId = models.IntegerField(primary_key=True)
    departureDate = models.DateTimeField(auto_now=False,null=True)
    arrivalDate = models.DateTimeField(auto_now=False,null=True)
    flightNumber = models.CharField(max_length=20)
    dcity = models.CharField(max_length=20)
    dcityName = models.CharField(max_length=20,null=True)
    acity = models.CharField(max_length=20)
    acityName = models.CharField(max_length=20,null=True)
    price = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    url = models.CharField(max_length=150)
# Create your models here.