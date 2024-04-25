from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Ticket,Appointment
from configcode import getid2,getid4,getid6,getid13
from fp.models import AccountBalance,Transaction
from ap.models import Promocode,Activation
import time,datetime
@login_required
@csrf_exempt
def da(request):
    print(request.POST)
    menu=request.POST.get('menu')
    tickets=request.POST.get('tickets')
    appointments=request.POST.get('appointments')
    projects=request.POST.get('projects')
    queries=request.POST.get('queries')
    if menu:
        my_dict = {}
        return render(request,'da/damenu.html',context=my_dict)
    if tickets:
        user=request.user
        token=request.POST.get('token')
        tickets=Ticket.objects.filter(account=user,status='open')
        ticket=request.POST.get('ticket')
        if ticket:
            allowed=0
            token1=0
            valid=0
            try:
                print("hello developer")
                token1=Promocode.objects.get(code=str(token))
                print('helo developer')
                valid=1
                balance=AccountBalance.objects.get(account=user)
            
                if balance.amount>=20:
                    allowed=1
            except:
                token1=token
                valid=0
            print('appointment request recieved:')
            ticket=Ticket.objects.get(ticketid=ticket)
            confirm=request.POST.get('confirm')
            if confirm:
#                try:
#                    discount1=Promocode.objects.get(code=token)
#                    balance.amount=balance.amount-18
#                    balance.save()
#                    Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Outsource Payment',amount=18,date = datetime.datetime.now(),staffid=request.user,reference=task)
#                    balance=AccountBalance.objects.get(account=discount1.account)
#                    balance.amount=balance.amount+8
#                    balance.save()
#                    Activation.objects.create(activationid=getid13(),product='Picta.com',account=discount1.account,payout=8)
#                    Transaction.objects.create(transactionid=getid6(),account=discount1.account,transactiontype='outsource Commission',amount=8,date = datetime.datetime.now(),staffid=request.user,reference=token)
#                
#                except:
#                    print('discount1 404')
#                    balance.amount=balance.amount-20
#                    Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Outsource Payment',amount=20,date = datetime.datetime.now(),staffid=request.user,reference=task)
#                    
#                    balance.save()
            
                try:
                    print('appointment confirmed test')
                    discount1=Promocode.objects.get(code=str(token))
                    balance=AccountBalance.objects.get(account=user)
                    balance.amount=balance.amount-18
                    balance.save()
                    print('appointment confirmed test')
                    Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Appointment Payment',amount=18,date = datetime.datetime.now(),staffid=request.user,reference=token)
                    balance=AccountBalance.objects.get(account=discount1.account)
                    balance.amount=balance.amount+8
                    balance.save()
                    print('appointment confirmed test')
                    Activation.objects.create(activationid=getid13(),product='Picta.com',account=discount1.account,payout=8)
                    Transaction.objects.create(transactionid=getid6(),account=discount1.account,transactiontype='Appointment Commission',amount=8,date = datetime.datetime.now(),staffid=request.user,reference=token)
                    print('appointment confirmed test')
                except:
                    balance=AccountBalance.objects.get(account=user)
                    balance.amount=balance.amount-20
                    balance.save()
                    Transaction.objects.create(transactionid=getid6(),account=user,transactiontype='Appointment Payment',amount='20',date = datetime.datetime.now(),staffid=user,reference='Appointment')
                Appointment.objects.create(appointmentid=getid4(),ticket=ticket,account=user,task=ticket.task)
                print('appointment confirmed')
                ticket.status='appointment'
                ticket.save()
                tickets=Ticket.objects.filter(account=user,status='open')
                my_dict = {'tickets':tickets}
                return render(request,'da/datickets.html',context=my_dict)
            balance=AccountBalance.objects.get(account=user)
            
            if balance.amount>=20:
                allowed=1
            my_dict={'ticket':ticket,'balance':balance,'allowed':allowed,'valid':valid,'token':token}
            return render(request,'da/confirmappointment.html',context=my_dict)
            
            
        my_dict = {'tickets':tickets}
        return render(request,'da/datickets.html',context=my_dict)
    if appointments:
        user=request.user
        appointments=Appointment.objects.filter(account=user)
        
        my_dict = {'appointments':appointments}
        return render(request,'da/daappointments.html',context=my_dict)
    if projects:
        my_dict = {}
        return render(request,'da/daprojects.html',context=my_dict)
    if queries:
        my_dict = {}
        return render(request,'da/daqueries.html',context=my_dict)
    
    my_dict = {}
    return render(request,'da/da.html',context=my_dict)