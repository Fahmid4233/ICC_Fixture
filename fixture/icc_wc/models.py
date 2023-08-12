from django.db import models

# Create your models here.
class Iccfixture(models.Model):
    team1 = models.CharField(max_length=25)
    team2 = models.CharField(max_length=25)
    date = models.CharField(max_length=25)
    days = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    venue = models.CharField(max_length=25)