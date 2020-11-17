from django.db import models

# Create your models here.
class Wxuser(models.Model):
    id = models.AutoField(primary_key=True)
    openid=models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    #gender = models.CharField(max_length=50)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.openid

class concernFlight(models.Model):
    openid = models.ForeignKey('Wxuser',on_delete=models.CASCADE)
    departureDate = models.DateTimeField(auto_now=False, null=True)
    arrivalDate = models.DateTimeField(auto_now=False, null=True)
    flightNumber = models.CharField(max_length=20)
    dcity = models.CharField(max_length=20)
    acity = models.CharField(max_length=20)
    price = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    url = models.CharField(max_length=150)