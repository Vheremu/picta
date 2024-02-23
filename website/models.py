from django.db import models
from django.contrib.auth.models import User
from configcode import getid
class Feedback(models.Model):
    feedbackid = models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,related_name='user',null=True,on_delete=models.SET_NULL)
    service = models.CharField(blank=False,max_length=11,unique=False)
    rating = models.IntegerField(blank=False,unique=False)
    comment = models.CharField(blank=False,max_length=50 ,unique=False)
    def __str__(self):
        return self.comment
class Contact(models.Model):
    contactid = models.IntegerField(blank=False,unique=True,primary_key=True)
    username=models.CharField(blank=False,max_length=100,unique=False)
    email=models.CharField(blank=False,max_length=100,unique=False)
    company=models.CharField(blank=False,max_length=100,unique=False)
    employees=models.CharField(blank=False,max_length=100,unique=False)
    reoson=models.CharField(blank=False,max_length=100,unique=False)
    def __str__(self):
        return self.reoson
    
# Create your models here.
