"""
URL configuration for picta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
app_name = 'picta_app'
urlpatterns = [
    path("pictakeyadmin/", admin.site.urls),
    path('',include('website.urls'),name='website'),
    path('accounts/',include('accounts.urls'),name='accounts'),
    path('pa/',include('pa.urls'),name='pa'),
    path('da/',include('da.urls'),name='da'),
    path('ap/',include('ap.urls'),name='ap'),
    path('fp/',include('fp.urls'),name='fp'),
    path('sa/',include('sa.urls'),name='sa'),
]
