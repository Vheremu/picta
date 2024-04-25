from django.contrib import admin
from django.urls import path,include
from ap import views,urls
app_name = 'ap_app'
urlpatterns = [
    path('',views.ap,name='ap'),
    path('myadds',views.myadds,name='myadds'),
    path('myaccount',views.myaccount,name='myaccount'),
    path('listadds',views.listadds,name='listadds'),
]
