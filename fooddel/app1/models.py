from django.db import models
from django.utils.text import slugify


class userInfo(models.Model):
    usernames = models.CharField(max_length=50)
    emmails = models.EmailField(max_length=30)
    dob=models.DateField(max_length=30)

