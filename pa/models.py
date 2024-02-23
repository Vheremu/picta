from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    taskid= models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(blank=True,max_length=100,unique=True)
    description=models.CharField(blank=True,max_length=100,unique=False)
    frequency=models.CharField(blank=True,max_length=100,unique=False)
    time=models.IntegerField(blank=True,unique=False)
    cost=models.IntegerField(blank=True,unique=False)
    nature=models.CharField(blank=False,unique=False,max_length=50)
    def __str__(self):
        return self.name
# Create your models here.

#from django.db import models
#from django.contrib.auth.models import User
## Create your models here.
#class UserProfileInfo(models.Model):
#    user = models.OneToOneField(User,on_delete=models.CASCADE)
#    phonenumber = models.CharField(blank=True,max_length=50,unique=True)
#    profile_pic = models.ImageField(upload_to='static/profile_pics',blank=True)
#
#    def __str__(self):
#        return self.user.username
#class Feedback(models.Model):
#    feedbackid = models.IntegerField(blank=False,unique=True,primary_key=True)
#    account = models.ForeignKey(User,related_name='user',null=True,on_delete=models.SET_NULL)
#    service = models.CharField(blank=False,max_length=11,unique=False)
#    rating = models.IntegerField(blank=False,unique=False)
#    comment = models.CharField(blank=False,max_length=50 ,unique=False)
#    def __str__(self):
#        return self.comment