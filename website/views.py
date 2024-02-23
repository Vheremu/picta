from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Feedback,Contact
from configcode import getid,getid1
# Create your views here.
def index(request):
    my_dict = {}
    return render(request,'website/index.html',context=my_dict)
@login_required
def services(request):
    my_dict = {}
    return render(request,'website/services.html',context=my_dict)
@login_required
def feedback(request):
    x=request.POST
    print(x)
    service=request.POST.get('service')
    rating=request.POST.get('stars')
    comment=request.POST.get('comment')
    user= request.user
    error=''
    if request.POST:
        if user:
            if service:
                if rating:
                    num=getid()
                    Feedback.objects.create(feedbackid=num,account=user,service=service,rating=rating,comment=comment)
                    if comment:print('request recieved');error='Feedback Submited.'
                    else:print('please select comment');error='Leave comment.';
                else:print('please select rating');error='Pick rating.';
            else:print('please select service');error='Pick service.';
        else:
            print('No Registered User');error='Sign In.';
    my_dict = {'error':error}
    return render(request,'website/feedback.html',context=my_dict)
def contactus(request):
    x=request.POST
    print(x)
    username=request.POST.get('username')
    email=request.POST.get('email')
    company=request.POST.get('company')
    employees=request.POST.get('employees')
    reoson=request.POST.get('reoson')
    error=''
    if request.POST:
        if username:
            if email:
                if reoson:num=getid1();Contact.objects.create(contactid=num,username=username,email=email,company=company,employees=employees,reoson=reoson);print('feedback sent');error='Contact made';
                else:print('please enter a reoson');error='Enter reoson';
            else:print('please enter a email');error='Enter email';
        else:print('please enter a username');error='Enter Full Name';
    my_dict = {'error':error}
    return render(request,'website/contactus.html',context=my_dict)
def about(request):
    my_dict = {}
    return render(request,'website/about.html',context=my_dict)
def login(request):
    x=request.POST
    print(x)
    my_dict = {}
    return render(request,'website/login.html',context=my_dict)
def register(request):
    x=request.POST
    print(x)


    my_dict = {}
    return render(request,'website/register.html',context=my_dict)
