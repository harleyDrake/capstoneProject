from django.db import models

class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    platform = models.CharField(max_length=10, blank=True)
    year = models.IntegerField(blank=True)
    genre = models.CharField(max_length=128, blank=True)
    publisher = models.CharField(max_length=128, blank=True)
    euSales = models.FloatField()
    jpSales = models.FloatField()
    otherSales = models.FloatField()
    naSales = models.FloatField()
    globalSales = models.FloatField()
