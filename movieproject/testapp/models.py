from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=20)
    heroname=models.CharField(max_length=20)
    heroinname=models.CharField(max_length=20)
    rating=models.FloatField()
