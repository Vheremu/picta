from django.contrib import admin
from django.urls import path,include
from da import views,urls
app_name = 'da_app'
urlpatterns = [
    path('',views.da,name='da'),
]
