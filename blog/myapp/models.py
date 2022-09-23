from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
# from django.contrib.auth.models import AbstractUser
# Create your models here.


class Addpost(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=70)
    desc = models.TextField(max_length=300)
    date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.fname


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.ForeignKey(Addpost, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=75)
    created_on = models.DateTimeField(auto_now_add=True)

    def short_comment(self):
        return truncatechars(self.comment, 35)

    def __str__(self):
        return self.title.title
