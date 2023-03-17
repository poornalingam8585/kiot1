from django.db import models

# Create your models here.
class userdetails(models.Model):
  	name = models.CharField(default="", max_length=500, null=True,blank=True)
  	email = models.CharField(default="", max_length=500, null=True,blank=True)
  	subject = models.CharField(default="", max_length=500, null=True,blank=True)