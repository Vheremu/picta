from django.contrib import admin
from django.urls import path, include
from website import views,urls
app_name = 'website_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('feedback',views.feedback,name='feedback'),
    path('contactus',views.contactus,name='contactus'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    
]