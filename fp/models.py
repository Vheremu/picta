from django.db import models
from django.contrib.auth.models import User
class Pop(models.Model):
    popid= models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,on_delete=models.CASCADE)
    pop = models.ImageField(upload_to='static/pops',blank=False)
    def __str__(self):
        return self.account.username
class Transaction(models.Model):
    transactionid=models.IntegerField(blank=False,unique=True,primary_key=True)
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    transactiontype=models.CharField(blank=False,unique=False,max_length=50)
    amount= models.IntegerField(blank=False,unique=False,primary_key=False)
    date= models.DateTimeField(verbose_name='date',null=True)
    reference=models.CharField(blank=True,unique=False,primary_key=False,max_length=50)
    staffid=models.ForeignKey(User,on_delete=models.CASCADE,related_name='staffid')
    def __str__(self):
        return self.account.username
class AccountBalance(models.Model):
    accountbalanceid=models.IntegerField(blank=False,unique=True,primary_key=True)
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.IntegerField(blank=False,unique=False,primary_key=False)
    def __str__(self):
        return self.account.username
class EcocashWithdrawal(models.Model):
    ecocashwithdrawalid=models.IntegerField(blank=False,unique=True,primary_key=True)
    number=models.CharField(blank=False,unique=False,max_length=50)
    currency=models.CharField(default='ZiG',blank=False,unique=False,max_length=50)
    amount=models.IntegerField(blank=False,unique=False,primary_key=False)
    date= models.DateTimeField(verbose_name='date',null=True)
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(blank=False,unique=False,max_length=50)
    def __str__(self):
        return self.account.username
class ZipitWithdrawal(models.Model):
    zipitwithdrawalid=models.IntegerField(blank=False,unique=True,primary_key=True)
    number=models.CharField(blank=False,unique=False,max_length=50)
    currency=models.CharField(default='ZiG',blank=False,unique=False,max_length=50)
    amount=models.IntegerField(blank=False,unique=False,primary_key=False)
    date= models.DateTimeField(verbose_name='dates',null=True)
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    financialinstitution=models.CharField(default='',blank=False,unique=False,max_length=50)
    status=models.CharField(blank=False,unique=False,max_length=50,default='')
    def __str__(self):
        return self.account.username