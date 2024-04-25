from django.contrib import admin
from django.urls import path,include
from sa import views,urls
app_name = 'sa_app'
urlpatterns = [
    path('',views.sa,name='sa'),
]
