from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Ticket,Appointment
from configcode import getid2,getid4
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
        tickets=Ticket.objects.filter(account=user,status='open')
        ticket=request.POST.get('ticket')
        if ticket:
            print('appointment request recieved:')
            ticket=Ticket.objects.get(ticketid=ticket)
            confirm=request.POST.get('confirm')
            if confirm:
                Appointment.objects.create(appointmentid=getid4(),ticket=ticket,account=user,task=ticket.task)
                print('appointment confirmed')
                ticket.status='appointment'
                ticket.save()
                tickets=Ticket.objects.filter(account=user,status='open')
                my_dict = {'tickets':tickets}
                return render(request,'da/datickets.html',context=my_dict)
            my_dict={'ticket':ticket}
            return render(request,'da/confirmappointment.html',context=my_dict)
            
            
        my_dict = {'tickets':tickets}
        return render(request,'da/datickets.html',context=my_dict)
    if appointments:
        my_dict = {}
        return render(request,'da/daappointments.html',context=my_dict)
    if projects:
        my_dict = {}
        return render(request,'da/daprojects.html',context=my_dict)
    if queries:
        my_dict = {}
        return render(request,'da/daqueries.html',context=my_dict)
    
    my_dict = {}
    return render(request,'da/da.html',context=my_dict)