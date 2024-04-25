from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from fp.models import AccountBalance,Transaction
from ap.models import Promocode,Activation
from configcode import getid2,getid3,getid13,getid6
from .models import Task
from da.models import Ticket
import time,datetime
# Create your views here.
@login_required
@csrf_exempt
def dashboard(request):
    my_dict = {}
    return render(request,'pa/dashboard.html',context=my_dict)
@login_required
@csrf_exempt
def myworkday(request):
    my_dict = {}
    print(request.POST)
    submittask=request.POST.get('submittask')
    menu=request.POST.get('menu')
    addtask=request.POST.get('addtask')
    alltasks=request.POST.get('alltasks')
    dailytasks=request.POST.get('dailytasks')
    weeklytasks=request.POST.get('weeklytasks')
    monthlytasks=request.POST.get('monthlytasks')
    autocomplete=request.POST.get('autocomplete')
    if request.POST:
        if autocomplete:
            print('automate')
            my_dict={'autocomplete':'1'}
            print('autocomplete activated')
            return render(request,'pa/myworkdayaddtask.html',context=my_dict)
        taskname=request.POST.get('taskname')
        cost=request.POST.get('cost')
        nature=request.POST.get('nature')
        if submittask :
            if not nature:
                my_dict={'nature':'Please Enter A Valid Task Nature'}
                print('Invalid Nature')
                return render(request,'pa/myworkdayaddtask.html',context=my_dict)
            if not taskname:
                my_dict={'comment':'Please Enter A Valid Task Name'}
                print('Invalid Name')
                return render(request,'pa/myworkdayaddtask.html',context=my_dict)
            if not cost:
                my_dict={'cost':'Please Enter A Valid Cost'}
                print('Invalid Cost')
                return render(request,'pa/myworkdayaddtask.html',context=my_dict)
            taskid=getid2()
            user=request.user
            taskname=request.POST.get('taskname')
            description=request.POST.get('description')
            frequency=request.POST.get('frequency')
            time=request.POST.get('time')
            cost=request.POST.get('cost')
            nature=request.POST.get('nature')
            if time=='<60':
                time=60
            elif time=='<10':
                time=10
            elif time=='<30':
                time=30
            elif time=='<120':
                time=120
            else:
                time=240
            if cost=='<10':
                cost=10
            elif cost=='<30':
                cost=30
            elif cost=='<100':
                cost=100
            elif cost=='<200':
                cost=200
            else:
                cost=400
            try:
                Task.objects.create(taskid=taskid,account=user,name=taskname,description=description,frequency=frequency,time=time,cost=cost,nature=nature)
            except:
                print('task not added')
                my_dict={'added':'Enter a unique Task Name'}
                return render(request,'pa/myworkdayaddtask.html',context=my_dict)
                
            
            print('task added')
            my_dict={'added':'Successfully Added Task'}
            return render(request,'pa/myworkdayaddtask.html',context=my_dict)
        
    if menu:
        user=request.user
        tasks=Task.objects.filter(account=user)
        total=0
        for task in tasks:
            total=total+1
        dailys=Task.objects.filter(account=user,frequency='daily')
        daily=0
        for d in dailys:
            daily=daily+1
        weeklys=Task.objects.filter(account=user,frequency='weekly')
        weekly=0
        for w in weeklys:
            weekly=weekly+1
        monthlys=Task.objects.filter(account=user,frequency='monthly')
        monthly=0
        for m in monthlys:
            monthly=monthly+1
        manuals=Task.objects.filter(account=user,nature='manual')
        manual=0
        for m in manuals:
            manual=manual+1
        digitals=Task.objects.filter(account=user,nature='digital')
        digital=0
        for d in digitals:
            digital=digital+1
        automateds=Task.objects.filter(account=user,nature='automated')
        automated=0
        for a in automateds:
            automated=automated+1
        outsourceds=Task.objects.filter(account=user,nature='outsourced')
        outsourced=0
        for o in outsourceds:
            outsourced=outsourced+1
        sourceds=Task.objects.filter(account=user,nature='sourced')
        sourced=0
        for o in sourceds:
            sourced=sourced+1
        my_dict={'menu':menu,'user':user,'total':total,'daily':daily,'weekly':weekly,'monthly':monthly,'manual':manual,'digital':digital,'automated':automated,'outsourced':outsourced,'sourced':sourced}
        print('menu')
        return render(request,'pa/myworkdaymenu.html',context=my_dict)
    if addtask:
        my_dict={'addtask':addtask}
        print('addtask')
        return render(request,'pa/myworkdayaddtask.html',context=my_dict)
    if  alltasks:
        user=request.user
        digitalize=request.POST.get('digitalize')
        if digitalize:
            confirmdigitalize=request.POST.get('confirmdigitalize')
            
            task=Task.objects.get(taskid=digitalize)
            if confirmdigitalize:
                Ticket.objects.create(ticketid=getid3(),account=user,task=task,request='digitalize',status='open')
                task.nature='pendingdigitalization'
                task.save()
                my_dict={'task':task,'comment':'Successfully Opened Task Digitalization Ticket!'}
                return render(request,'pa/myworkdayalltasks.html',context=my_dict)
            balance=AccountBalance.objects.get(account=user)
            print(balance.amount)
            my_dict={'task':task,'user':user,'balance':balance}
            return render(request,'pa/confirmdigitalization.html',context=my_dict)
        tasks=Task.objects.filter(account=user,nature='manual')
        my_dict={
            'tasks':tasks
        }
        return render(request,'pa/myworkdayalltasks.html',context=my_dict)
    if dailytasks:
        user=request.user
        automate=request.POST.get('automate')
        if automate:
            confirmautomate=request.POST.get('confirmautomate')
            task=Task.objects.get(taskid=automate)
            if confirmautomate:
                print('helo world')
                Ticket.objects.create(ticketid=getid3(),account=user,task=task,request='automate',status='open')
                task.nature='pendingautomation'
                task.save()
                my_dict={'task':task,'comment':'Successfully Opened Task Automation Ticket!'}
                return render(request,'pa/myworkdaydailytasks.html',context=my_dict)
            
            my_dict={'task':task}
            
            return render(request,'pa/confirmautomation.html',context=my_dict)
        
        tasks=Task.objects.filter(account=user,nature='digital')
        my_dict={'tasks':tasks}
        print('dailytasks')
        return render(request,'pa/myworkdaydailytasks.html',context=my_dict)
    if weeklytasks:
        user=request.user
        tasks2=Task.objects.filter(account=user,nature='pendingautomation') 
        tasks=Task.objects.filter(account=user,nature='digital')
        outsource=request.POST.get('outsource')
        if outsource:
            confirmoutsource=request.POST.get('confirmoutsource')
            token=request.POST.get('token')
            print(token)
            task=Task.objects.get(taskid=int(outsource))
            print(task.taskid)
            if confirmoutsource:
                print('helo world')
                token=request.POST.get('token')
                balance=AccountBalance.objects.get(account=request.user)
                try:
                    discount1=Promocode.objects.get(code=token)
                    balance.amount=balance.amount-18
                    balance.save()
                    Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Outsource Payment',amount=18,date = datetime.datetime.now(),staffid=request.user,reference=task)
                    balance=AccountBalance.objects.get(account=discount1.account)
                    balance.amount=balance.amount+8
                    balance.save()
                    Activation.objects.create(activationid=getid13(),product='Picta.com',account=discount1.account,payout=8)
                    Transaction.objects.create(transactionid=getid6(),account=discount1.account,transactiontype='outsource Commission',amount=8,date = datetime.datetime.now(),staffid=request.user,reference=token)
                
                except:
                    print('discount1 404')
                    balance.amount=balance.amount-20
                    Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Outsource Payment',amount=20,date = datetime.datetime.now(),staffid=request.user,reference=task)
                    
                    balance.save()
                
                
                
                Ticket.objects.create(ticketid=getid3(),account=user,task=task,request='outsource',status='open')
                task.nature='pendingoutsource'
                task.save()
                user=request.user
                tasks=Task.objects.filter(account=user,nature='digital')
                my_dict={'task':task,'comment':'Successfully Opened Task Outsource Ticket!','tasks':tasks,'user':user}
                return render(request,'pa/myworkdayweeklytasks.html',context=my_dict)
            balance=AccountBalance.objects.get(account=user)
            allowed = 0
            discount=0
            try:
                print('error occured 1')
                discount=Promocode.objects.get(code=token)
                print('error occured 2')
                        
                        
                
                discount=1
            except:
                print('error occured except')
                discount=0
            if balance.amount < 20:
                allowed=0
            else:
                allowed=1
            if balance.amount>=18:
                
                if token:
                    try:
                        print('error occured 1')
                        discount=Promocode.objects.get(code=token)
                        print('error occured 2')
                        
                        
                        allowed=1
                        discount=1
                    except:
                        print('error occured except')
                        discount=0
            print(balance.amount)
            my_dict={'task':task,'user':user,'balance':balance,'allowed':allowed,'discount':discount,'token':token}
            return render(request,'pa/confirmoutsourcing.html',context=my_dict)
       
        my_dict={'tasks':tasks,'tasks2':tasks2}
        print('weeklytasks')
        return render(request,'pa/myworkdayweeklytasks.html',context=my_dict)
    if monthlytasks:
        my_dict={'monthlytasks':monthlytasks}
        print('monthlytasks')
        return render(request,'pa/myworkdaymonthlytasks.html',context=my_dict)
    return render(request,'pa/myworkdayaddtask.html',context=my_dict)