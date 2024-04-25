from django.shortcuts import render
from fp.forms import POPFORM
import time,datetime
from fp.models import Pop,Transaction,AccountBalance,ZipitWithdrawal,EcocashWithdrawal
from configcode import getid5,getid6,getid7,getid8
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def fp(request):
    user=request.user
    print(request.POST)
    print(request.user)
    if request.POST:
        print(request.POST)
        try:
            Pop.objects.create(account=user,popid=getid5(),pop=request.FILES['pop'])
            my_dict = {'message1':'Successfully Uploaded POP'}
            print(my_dict)
        except:
            print('data did not validate')
            my_dict = {'message':'Please upload a valid POP! '}
        return render(request,'fp/uploadfunds.html',context=my_dict)

        
    my_dict = {}
    return render(request,'fp/uploadfunds.html',context=my_dict)
@login_required
def withdrawfunds(request):
    user=request.user
    ecocash=request.POST.get('type')
    zipit=request.POST.get('type')
    
    if ecocash=='Ecocash Withdrawal':
        print('withdrawal successfull')
        
        try:
            print(request.POST)
            amount=  request.POST.get('amount'     )
            if int(amount)<=1:
                print('failed to proccess withdrawal')
                message='Withdrawal Unsuccessfull. Please enter valid amount'
                my_dict={'message':message}
                return render(request,'fp/withdrawfunds.html',context=my_dict)
            
            balance=AccountBalance.objects.get(account=user)
            
            balance.amount=balance.amount-int(amount)
            if balance.amount<=20:
                message='Insufficient Funds'
                my_dict={'message':message}
                return render(request,'fp/withdrawfunds.html',context=my_dict)
            print('helo world')
            balance.save()
            EcocashWithdrawal.objects.create(ecocashwithdrawalid=getid7(),number=request.POST.get('number'),amount=amount,date=datetime.datetime.now(),account=user,status='open',currency=request.POST.get('currency'))
            Transaction.objects.create(transactionid=getid6(),account=user,transactiontype=request.POST.get('type'),amount=amount,date = datetime.datetime.now(),staffid=user,reference=request.POST.get('number'))
        except:
            print('failed to proccess withdrawal')
            message='Withdrawal Unsuccessfull. Please enter valid information'
            my_dict={'message':message}
            return render(request,'fp/withdrawfunds.html',context=my_dict)
    if zipit=='Zipit Withdrawal':
        print(request.POST)
        try:
            amount=request.POST.get('amount')
            print(amount)
            if int(amount)<=1:
                print('failed to proccess withdrawal')
                message1='Withdrawal Unsuccessfull. Please enter valid amount'
                my_dict={'message1':message1}
                return render(request,'fp/withdrawfunds.html',context=my_dict)
            balance=AccountBalance.objects.get(account=user)
            
            balance.amount=balance.amount-int(amount)
            if balance.amount<=20:
                message1='Insufficient Funds'
                my_dict={'message1':message1}
                return render(request,'fp/withdrawfunds.html',context=my_dict)
            currency=request.POST.get('currency')
            print(currency)
            amount=int(request.POST.get('amount'))
            print(amount)
            number=request.POST.get('number')
            print(number)
            financialinstritution=request.POST.get('financialinstitution')
            print(financialinstitution)
            print('helo world')
            balance.save()
            
            ZipitWithdrawal.objects.create(zipitwithdrawalid=getid8(),number=number,amount=int(amount),account=user,status='open',currency=currency,financialinstitution=financialinstitution)
            print('helo world')
            Transaction.objects.create(transactionid=getid6(),account=user,transactiontype=request.POST.get('type'),amount=amount,date = datetime.datetime.now(),staffid=user,reference=request.POST.get('number'))
            print('Successfully proccessed withdrawal')
            message1='Withdrawal successfull.'
            my_dict={'message1':message1}
            return render(request,'fp/withdrawfunds.html',context=my_dict)
        except:
            print('failed to proccess withdrawal')
            message1='Withdrawal Unsuccessfull. Please enter valid information'
            my_dict={'message1':message1}
            return render(request,'fp/withdrawfunds.html',context=my_dict)
    my_dict={}
    return render(request,'fp/withdrawfunds.html',context=my_dict)
@login_required
def myaccount(request):
    user=request.user
    objects=Transaction.objects.filter(account=request.user)
    balance=AccountBalance.objects.get(account=request.user)
    print(user)
    print(objects)
    
    my_dict={'transaction':objects,'balance':balance}
    return render(request,'fp/myaccount.html',context=my_dict)