from django.db import models
from django.contrib.auth.models import User
from pa.models import Task
class Ticket(models.Model):
    ticketid= models.IntegerField(blank=False,unique=True,primary_key=True)
    account = models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    request=models.CharField(blank=True,max_length=100,unique=False)
    opendate=models.DateTimeField(auto_now_add=True)
    closingdate=models.DateTimeField(null=True,blank=True,auto_now_add=False)
    status=models.CharField(blank=True,max_length=100,unique=False)
    def __str__(self):
        return self.task.name
class Appointment(models.Model):
    appointmentid=models.IntegerField(blank=False,unique=True,primary_key=True)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    date=models.DateTimeField(null=True,blank=True,auto_now_add=False)