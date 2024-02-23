from django.contrib import admin
from django.urls import path,include
from pa import views,urls
app_name = 'pa_app'
urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('myworkday',views.myworkday,name='myworkday'),
]
