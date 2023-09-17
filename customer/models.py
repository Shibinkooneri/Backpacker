from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.
class UserUploads(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='user_uploads',verbose_name='Upload Images')
    location=models.CharField(max_length=100,null=True)
    date=models.DateField(auto_now_add=True,null=True)

class Profilepictures(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Pic=models.ImageField(upload_to='profile_pics',verbose_name='profile pics')
    Homeloc=models.CharField(max_length=100,verbose_name="Home Location",null=True)

class TravelInvites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Destination=models.CharField(max_length=100,null=True)
    Location=models.CharField(max_length=100,verbose_name="Starting Location",null=True)
    Description=models.CharField(max_length=500,null=True)
    date=models.DateField(auto_now_add=True,null=True)

class Room(models.Model):
    invite=models.ForeignKey(TravelInvites,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)

class Message(models.Model):
    room=models.ForeignKey(Room,related_name='messages',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE,null=True)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)