from datetime import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
from django.template.backends import django


# class City(models.Model):
#     name=models.CharField(max_length=25)
#
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural='cities'

class WeatherData(models.Model):
    name=models.CharField(max_length=20)
    temp=models.FloatField()
    description=models.CharField(max_length=100)
    icon=models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    date=models.DateField(default=timezone.now,blank=True)

    class Meta:
        db_table="weather_data"