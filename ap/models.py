from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import time,datetime
#class Ticket(models.Model):
#    ticketid= models.IntegerField(blank=False,unique=True,primary_key=True)
#    account = models.ForeignKey(User,on_delete=models.CASCADE)
#    task=models.ForeignKey(Task,on_delete=models.CASCADE,blank=True)
#    request=models.CharField(blank=True,max_length=100,unique=False)
#    opendate=models.DateTimeField(auto_now_add=True)
#    closingdate=models.DateTimeField(null=True,blank=True,auto_now_add=False)
#    status=models.CharField(blank=True,max_length=100,unique=False)
#    def __str__(self):
#        return self.task.name
class Listadd(models.Model):
    listaddid= models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,on_delete=models.CASCADE)
    opendate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.account.username
class Add(models.Model):
        addid= models.IntegerField(blank=False,unique=True,primary_key=True)
        account = models.ForeignKey(User,on_delete=models.CASCADE)  
        image = models.ImageField(upload_to='static/adds',blank=False)
        cost = models.IntegerField(blank=False,unique=False,primary_key=False)
        payout = models.IntegerField(blank=False,unique=False,primary_key=False)
        company=models.CharField(blank=True,max_length=100,unique=False)
        def __str__(self):
            return self.account.username
class Promocode(models.Model):
        promocodeid= models.IntegerField(blank=False,unique=True,primary_key=True)
        code = models.CharField(max_length=100,blank=False,unique=False,primary_key=False)
        account = models.ForeignKey(User,on_delete=models.CASCADE) 
        opendate=models.DateTimeField(auto_now_add=True)
        product=models.CharField(blank=True,max_length=100,unique=False)
        def __str__(self):
            return self.account.username
class Activation(models.Model):
    activationid=models.IntegerField(blank=False,unique=True,primary_key=True)
    product=models.CharField(blank=True,max_length=100,unique=False)
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    payout=models.IntegerField(blank=False,unique=False,primary_key=False)
    
    def __str__(self):
            return self.account.username
    
class Rank(models.Model):
    rankid=models.IntegerField(blank=False,unique=True,primary_key=True)
    name=models.CharField(blank=True,max_length=100,unique=False)
    recruit =models.IntegerField(blank=False,unique=False,primary_key=False)
    branchsize=models.IntegerField(blank=False,unique=False,primary_key=False)
    responsibility=models.CharField(blank=True,max_length=100,unique=False)
    def __str__(self):
            return self.name
class Myaccount(models.Model):
    myaccountid=models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,on_delete=models.CASCADE,related_name='account')
    rank = models.ForeignKey(Rank,on_delete=models.CASCADE) 
    recruitedby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='daterecruited')
    datecreated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.account.username
class InvitationToken(models.Model):
    invitationid=models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,on_delete=models.CASCADE) 
    token=models.CharField(blank=True,max_length=100,unique=False)
    opendate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.account.username
class Reportto(models.Model):
    reporttoid=models.IntegerField(blank=False,unique=True,primary_key=True)
    account=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reporttoaccount')
    reportto=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reportto')
    def __str__(self):
            return self.account.username
        
        

    