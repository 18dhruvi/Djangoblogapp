from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=230)
    desc = models.TextField()
    # user=models.ForeignKey(User, on _delete=models.CASCADE)


class Addpost(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=50)
    date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Contact(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    subject = models.CharField(max_length=15)
    