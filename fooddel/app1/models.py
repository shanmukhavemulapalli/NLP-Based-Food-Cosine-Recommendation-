from django.db import models
from django.utils.text import slugify


class userInfo(models.Model):
    usernames = models.CharField(max_length=50)
    emmails = models.EmailField(max_length=30)
    dob=models.DateField(max_length=30)

class Ordn(models.Model):
    name= models.CharField(max_length=200)
    type= models.CharField(max_length=500)
    cuisine= models.CharField(max_length=400)
    address= models.CharField(max_length=700)

class Order(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=500)
    #cusine should be in array format 
    cusine = models.CharField(max_length=400)
    address = models.CharField(max_length=700)