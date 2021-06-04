from django.db import models
from django.contrib.auth.models import User

#Create your models here.

class Catogorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    img3 = models.ImageField(upload_to='pics')
    starring = models.CharField(max_length=100)
    creators = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField()
    year = models.IntegerField()
    category = models.ForeignKey(Catogorie, on_delete=models.CASCADE, null=True, related_name='video_category')

    def __str__(self):
        return self.name

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    cardnumber = models.IntegerField()
    expirydate = models.IntegerField()
    securitycode = models.IntegerField()

    def __str__(self):
        return self.name