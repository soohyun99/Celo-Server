from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class User(models.Model):
#    id = models.CharField(max_length=20, primary_key=True)
#    pw = models.TextField()
#    username = models.TextField()

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    location = models.TextField()
    desc = models.TextField()
    categ = models.TextField()
    period = models.TextField()
    hour = models.TextField()
    website = models.TextField()
    mainpic = models.ImageField(blank=True, upload_to="images", null=True)
    pic1 = models.ImageField(blank=True, upload_to="images", null=True)
    pic2 = models.ImageField(blank=True, upload_to="images", null=True)
    pic3 = models.ImageField(blank=True, upload_to="images", null=True)
    clap = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name="store", on_delete=models.CASCADE, null=True
    )

#class Login(models.Model):
#    id = models.CharField(max_length=20, primary_key=True)
#    pw = models.TextField()
#    email = models.TextField()
#    nickname = models.TextField()
#    store = models.ManyToManyField(Store, blank=True)

class Bigmarket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    location = models.TextField()
    pic = models.ImageField(blank=True, upload_to="images", null=True)
    store = models.ManyToManyField(Store, blank=True)