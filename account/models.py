from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registers(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    institution_email = models.CharField(max_length=200)
    graduation_year = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='pics', default="")

    def __str__(self):
        return self.firstname


class UnVerified(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    institution_email = models.CharField(max_length=200)
    graduation_year = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname


class Upload(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    profile_image = models.ImageField(upload_to='pics', default="")

    def __str__(self):
        return self.username
