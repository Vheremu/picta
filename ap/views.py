from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import time,datetime
from .models import Add,Promocode,Activation,Myaccount,InvitationToken,Rank,Reportto,Listadd
from fp.models import AccountBalance,Transaction
from imagecode import printpromo,printpromocode,saveimage
from configcode import getid11,getid12,getid6,getid14,getid15,getid16,getid17
from code import a1
# Create your views here.
@login_required
@csrf_exempt
def listadds(request):
    token=request.POST.get("token")
    notoken=request.POST.get("notoken")
    tokenconfirm=request.POST.get('tokenconfirm')
    confirm=request.POST.get('confirm')
    user=request.user
    balance=AccountBalance.objects.get(account=user)
    good=0
    if balance.amount>=5:
        good=1
    if notoken:
        print('no token')
        my_dict = {'balance':balance,'good':good}
        return render(request,'ap/confirmlistadd.html',context=my_dict)
    if confirm:
        print('confirm')
        if token:
            token=InvitationToken.objects.get(token=token)
            inviter=token.account
            inviteraccount=Myaccount.objects.get(account=inviter)
            inviterrank=inviteraccount.rank
            invitationpost=Rank.objects.get(rankid=(inviteraccount.rank.rankid+1))
            inviter=token.account
            inviteraccount=Myaccount.objects.get(account=inviter)
            inviterrank=inviteraccount.rank
            invitationpost=Rank.objects.get(rankid=(inviteraccount.rank.rankid+1))
            try:
                reportto=Reportto.objects.get(account=request.user)
                reportto.reportto=inviter
                reportto.save()
                
            except:
                reportto=Reportto.objects.create(reporttoid=getid16(),account=request.user,reportto=inviter)
                myaccount=Myaccount.objects.create(myaccountid=getid15(),account=request.user,rank=invitationpost,recruitedby=inviter,datecreated=datetime.datetime.now())
            
        balance.amount=balance.amount-5
        balance.save()
        Listadd.objects.create(listaddid=getid17(),account=user,opendate=datetime.datetime.now())
        message='Successfully Listed Add!'
        my_dict = {'message':message}
        return render(request,'ap/listadds.html',context=my_dict)
    if token:
        if tokenconfirm:
            valid=0
            
            try:
                token=InvitationToken.objects.get(token=tokenconfirm)
                print('token found')
                valid=1
            except:
                print('invalid token')
            
            my_dict = {'token':tokenconfirm,'valid':valid,'balance':balance,'good':good}
            return render(request,'ap/confirmlistadd.html',context=my_dict)
        my_dict = {'token':token}
        return render(request,'ap/tokenadd.html',context=my_dict)
    my_dict = {'token':token}
    return render(request,'ap/listadds.html',context=my_dict)
@login_required
@csrf_exempt
def ap(request):
    adds=Add.objects.filter(account=1)
    print(request.POST)
    confirm=request.POST.get('confirm')
    if confirm:
        token=request.POST.get('token')
        if token:
            token=InvitationToken.objects.get(token=token)
            inviter=token.account
            inviteraccount=Myaccount.objects.get(account=inviter)
            inviterrank=inviteraccount.rank
            invitationpost=Rank.objects.get(rankid=(inviteraccount.rank.rankid+1))
            inviter=token.account
            inviteraccount=Myaccount.objects.get(account=inviter)
            inviterrank=inviteraccount.rank
            invitationpost=Rank.objects.get(rankid=(inviteraccount.rank.rankid+1))
            try:
                reportto=Reportto.objects.get(account=request.user)
                reportto.reportto=inviter
                reportto.save()
            except:
                myaccount=Myaccount.objects.create(myaccountid=getid15(),account=request.user,rank=invitationpost,recruitedby=inviter,datecreated=datetime.datetime.now())
                reportto=Reportto.objects.create(reporttoid=getid16(),account=request.user,reportto=inviter)
            
        message='Successfully Purchased Add!'
        newadd=Add.objects.get(addid=int(confirm))
        promoid=getid12()
        Transaction.objects.create(transactionid=getid6(),account=request.user,transactiontype='Add Purchase',amount=newadd.cost,date = datetime.datetime.now(),staffid=request.user,reference=promoid)
        print(newadd.image)
        balance=AccountBalance.objects.get(account=request.user)
        balance.amount=balance.amount-newadd.cost
        balance.save()
        promocode=Promocode.objects.create(promocodeid=promoid,account=request.user,code=str(request.user.username)+str(promoid),product=newadd.company)
        image=printpromocode(newadd.image,promocode.code)
        print(image)
        image=image.save('static/adds/promo2'+promocode.code+'.png')
        Add.objects.create(addid=getid11(),account=request.user,image='static/adds/promo2'+promocode.code+'.png',cost=newadd.cost,payout=newadd.payout,company=newadd.company)

        
        my_dict = {'message':message,'adds':adds}
        return render(request,'ap/viewadds.html',context=my_dict)
    if request.POST:
        token=request.POST.get('token')
        valid=0
        if token:
            print('helo world')
            try:
                token=InvitationToken.objects.get(token=token)
#                inviter=token.account
#                inviteraccount=Myaccount.objects.get(account=inviter)
#                inviterrank=inviteraccount.rank
#                invitationpost=Rank.objects.get(rankid=(inviteraccount.rank.rankid+1))
                valid=1
#                try:
#                    myaccount=Myaccount.objects.get(account=request.user)
#                    print('account upgrade')
#                except:
#                    print('new registration')
#                    inviter=token.account
#                    inviteraccount=Myaccount.objects.get(account=inviter)
#                    inviterrank=inviteraccount.rank
#                    invitationpost=Rank.objects.get(rankid=(inviteraccount.rank.rankid+1))
       #             myaccount=Myaccount.objects.create(myaccountid=getid15(),account=request.user,rank=invitationpost,recruitedby=inviter,datecreated=datetime.datetime.now())
            except:
                print('404 invalid token')
        balance=AccountBalance.objects.get(account=request.user)
        good=0
        adds=request.POST.get('addid')
        adds=Add.objects.get(addid=adds)
        image=printpromo(adds.image)
        if balance.amount >= adds.cost:
            good = 1
        print(image)
        image='promo.png'
        my_dict = {'adds':adds,'balance':balance,'image':image,'good':good,'token':token,'valid':valid}
        return render(request,'ap/confirmbuyadd.html',context=my_dict)
    my_dict = {'adds':adds}
    return render(request,'ap/viewadds.html',context=my_dict)
@login_required
@csrf_exempt
def myadds(request):
    adds=Add.objects.filter(account=request.user)
    activations=Activation.objects.all()
    sales=0
    my_dict = {'adds':adds,'sales':sales}
    return render(request,'ap/myadds.html',context=my_dict)
@login_required
@csrf_exempt
def myaccount(request):
    user=request.user
    reportto=''
    try:
        reportto=Reportto.objects.get(account=user)
    except:
        reportto=0
    print(reportto)
    myaccount=0
    try:
        myaccount=Myaccount.objects.get(account=user)
    except:
        print('404 not member')
    print(myaccount)
    if request.POST:
        print(request.POST)
        firstname=request.POST.get('firstname')
        surname=request.POST.get('surname')
        houseaddress=request.POST.get('houseaddress')
        townaddress=request.POST.get('townaddress')
        invitee=request.POST.get('invitee')
        inviteesurname=request.POST.get('inviteesurname')
        if firstname:
            print('helo world')
            if surname:
                print('helo world')
                if houseaddress:
                    print('helo world')
                    if townaddress:
                        print('helo world')
                        if invitee:
                            print('helo world')
                            if inviteesurname:
                                print('helo world')
                                inviterpost=myaccount.rank.name
                                invitationpost=Rank.objects.get(rankid=(myaccount.rank.rankid+1))
                                invitationpostid=str(invitationpost.rankid)
                                invitationpost=invitationpost.name
                                num=getid14()
                                token='pictatoken'+str(request.user.username)+str(num)
                                InvitationToken.objects.create(invitationid=num,account=request.user,opendate=datetime.datetime.now(),token=token)
                                date=str(datetime.datetime.now())
                                a1(firstname,surname,houseaddress,townaddress,inviterpost,invitee,inviteesurname,invitationpost,invitationpostid,token,date)
                                message='Successfully Generated Invitation Letter for '+invitee+' .'
                                letter='success'
                                my_dict = {'myaccount':myaccount,'message':message,'letter':letter,'reportto':reportto}
                                return render(request,'ap/myaccount.html',context=my_dict)
                            else:
                                message='Please Enter All Required Details To Generate Invitation Letter.'
                                my_dict = {'myaccount':myaccount,'message':message,'reportto':reportto}
                                return render(request,'ap/myaccount.html',context=my_dict)
                        else:
                            message='Please Enter All Required Details To Generate Invitation Letter.'
                            my_dict = {'myaccount':myaccount,'message':message,'reportto':reportto}
                            return render(request,'ap/myaccount.html',context=my_dict)
                    else:
                        message='Please Enter All Required Details To Generate Invitation Letter.'
                        my_dict = {'myaccount':myaccount,'message':message,'reportto':reportto}
                        return render(request,'ap/myaccount.html',context=my_dict)
                else:
                    message='Please Enter All Required Details To Generate Invitation Letter.'
                    my_dict = {'myaccount':myaccount,'message':message,'reportto':reportto}
                    return render(request,'ap/myaccount.html',context=my_dict)
            else:
                message='Please Enter All Required Details To Generate Invitation Letter.'
                my_dict = {'myaccount':myaccount,'message':message,'reportto':reportto}
                return render(request,'ap/myaccount.html',context=my_dict)
        else:
            message='Please Enter All Required Details To Generate Invitation Letter.'
            my_dict = {'myaccount':myaccount,'message':message,'reportto':reportto}
            return render(request,'ap/myaccount.html',context=my_dict)
            
    my_dict = {'myaccount':myaccount,'reportto':reportto}
    return render(request,'ap/myaccount.html',context=my_dict)