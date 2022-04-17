from unicodedata import name
from django.db import models
from django.forms import DateField

from django.utils.timezone import now




class dealist(models.Model):
    
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    st = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    zip = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    short_name = models.CharField(max_length=60)
    full_name = models.CharField(max_length=60)

class mytable(models.Model):
    
    name = models.CharField(max_length=60)
    dealership = models.IntegerField()
    review = models.CharField(max_length=60)
    purchase = models.CharField(max_length=60)
    purchase_date = models.DateField()
    car_make = models.CharField(max_length=60)
    car_model = models.CharField(max_length=60)
    car_year = models.IntegerField()

