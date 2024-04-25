from django.contrib import admin
from django.urls import path,include
from fp import views,urls
app_name = 'fp_app'
urlpatterns = [
    path('',views.fp,name='fp'),
    path('withrawfunds',views.withdrawfunds,name='withdrawfunds'),
    path('myaccount',views.myaccount,name='myaccount'),
]
