import datetime
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Home(models.Model):
    text = models.TextField()
    picture = models.ImageField(upload_to = 'img', blank = True, null = True)


    def __str__(self):
        return self.text

class Clothes(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    picture = models.FileField(upload_to = 'img', blank = True, null = True)

class Customs(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    picture = models.ImageField(upload_to = 'img', blank = True, null = True)

class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    picture = models.ImageField(upload_to = 'img', blank = True, null = True)

    def __str__(self):
        return self.question       
 
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()
    discord_id = models.CharField(max_length=100)
    zoom_id = models.CharField(max_length=100)
    # password = models.CharField(widget=models.PasswordInput)
    # confirmation_password = models.CharField(widget=models.PasswordInput)


class stock(models.Model):
  date_time = models.DateTimeField(primary_key=True)
  price_low = models.FloatField()
  price_high = models.FloatField()


