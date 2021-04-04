from django.db import models

# Create your models here.
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    location = models.TextField()
    desc = models.TextField()
    mainpic = models.ImageField(blank=True, upload_to="images", null=True)
    pic1 = models.ImageField(blank=True, upload_to="images", null=True)
    pic2 = models.ImageField(blank=True, upload_to="images", null=True)
    pic3 = models.ImageField(blank=True, upload_to="images", null=True)
    clap = models.IntegerField()

class Login(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pw = models.TextField()
    email = models.TextField()
    nickname = models.TextField()
    store = models.ManyToManyField(Store, blank=True)