from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from fp.models import AccountBalance,Transaction
from .models import Website,Webpage
from da.models import Ticket
from pa.models import Task
from ap.models import Promocode,Activation
import time,datetime
from configcode import getid9,getid10,getid3,getid6,getid2,getid13
# Create your views here.
@login_required
@csrf_exempt
def sa(request):
    print(request.POST)
    confirm=request.POST.get('Confirm')
    htmlfiles=request.POST.get('htmlfiles')
    number=request.POST.get('number')
    if number:
        number=int(number)
        number1=number
        print(number)
        num=[]
        ids=int(1)
        while number>=1:
        
            num.append(ids)
            ids=ids+1
            number=number-1
        print(number1)
        number=num
        my_dict = {'number':number,'number1':number1}
        return render(request,'sa/index.html',context=my_dict)
    if htmlfiles:
        print('helloworld')
        name=request.POST.get('websitename')
        token=request.POST.get('token')
        website=Website.objects.create(websiteid=getid9(),account=request.user,name=name)
        
        balance=AccountBalance.objects.get(account=request.user)
        number1=request.POST.get('number1')
        num=int(number1)
        while num>=1:
            print(num)
            try:
                Webpage.objects.create(webpageid=getid10(),account=request.user,webpage=request.FILES[str(num)])
            except:
                print('error occured')
            num=num-1
            #ckeck if balance is sufficient and if a token is intered
        good=0
        discount=0
        if balance.amount>=18:
                if token:
                    try:
                        print('error occured 1')
                        discount=Promocode.objects.get(code=token)
                        print('error occured 2')
                        
                        
                        good=1
                    except:
                        print('error occured except')
                        discount=0
        elif balance.amount>=20:
            print('error occured 3')
            good=1
        else:
            good=0
            print('error occured 4')
            
        
        
                    
                    
        my_dict={'balance':balance,'number1':number1,'website':website,'good':good,'discount':discount}
        return render(request,'sa/confirmupload.html',context=my_dict)
    if confirm:
        print('upload confirmed')
        ids=getid2()
        task=Task.objects.create(taskid=ids,name=str(ids)+'seo'+str(request.user),account=request.user,description=request.POST.get('website'),frequency='daily',time=60,cost=200,nature='pendingautomation')
        discount=request.POST.get('discount')
        try:
            discount1=Promocode.objects.get(code=discount)
        except:
            print('discount1 404')
        balance=AccountBalance.objects.get(account=request.user)
        if discount:
            balance.amount=balance.amount-18
            balance.save()
        else:
            balance.amount=balance.amount-20
            balance.save()
        
        if discount:
            Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Seo Payment',amount=18,date = datetime.datetime.now(),staffid=request.user,reference=request.POST.get('website'))
            balance=AccountBalance.objects.get(account=discount1.account)
            balance.amount=balance.amount+8
            balance.save()
            Transaction.objects.create(transactionid=getid6(),account=discount1.account,transactiontype='Seo Commission',amount=8,date = datetime.datetime.now(),staffid=request.user,reference=request.POST.get('website'))
            Activation.objects.create(activationid=getid13(),product='Picta.com',account=discount1.account,payout=8)
            
        else:
            Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Seo Payment',amount=20,date = datetime.datetime.now(),staffid=request.user,reference=request.POST.get('website'))
        Ticket.objects.create(ticketid=getid3(),account=request.user,task=task,request='Seo',status='open')
        success='Successfully Opened Seo Ticket'
        my_dict = {'success':success}
        return render(request,'sa/index.html',context=my_dict)
    my_dict = {}
    return render(request,'sa/index.html',context=my_dict)