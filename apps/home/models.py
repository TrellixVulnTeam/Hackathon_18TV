# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User 
from django.db.models import BigAutoField

# Create your models here.
class Profile(models.Model):
    username=models.CharField( max_length=50)
    email=models.EmailField(max_length=50)
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    country=models.CharField( max_length=50)
    zip=models.CharField( max_length=6)
    age=models.CharField( max_length=50)
    disease=models.CharField( max_length=50)
    class Meta:
        db_table:"profile"

class Diseases(models.Model):
    name=models.CharField( max_length=50)
    description=models.CharField( max_length=250)
    symptom=models.CharField(max_length=250)
    precautions=models.CharField(max_length=250)
    cures=models.CharField(max_length=250)
    class Meta:
        db_table:"diseases"