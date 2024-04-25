from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class Feedback(models.Model):
#    feedbackid = models.IntegerField(blank=False,unique=True,primary_key=True)
#    account = models.ForeignKey(User,related_name='user',null=True,on_delete=models.SET_NULL)
#    service = models.CharField(blank=False,max_length=11,unique=False)
#    rating = models.IntegerField(blank=False,unique=False)
#    comment = models.CharField(blank=False,max_length=50 ,unique=False)
#    def __str__(self):
#        return self.comment
class Website(models.Model):
    websiteid=models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,related_name='usersss',null=True,on_delete=models.SET_NULL)
    name = models.CharField(blank=False,max_length=50,unique=False)
    def __str__(self):
        return self.account
class Webpage(models.Model):
    webpageid=models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,related_name='userss',null=True,on_delete=models.SET_NULL)
    webpage = models.ImageField(upload_to='static/webpages',blank=True,default='')
    def __str__(self):
        return self.account