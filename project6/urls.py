"""project6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from amarnath.views import*
from amarnadh1.views import*

urlpatterns = [
    path('admin/', admin.site.urls), #admin==sriram no
    path('sriram/',sriram,name='sriram'), #sriram==sriram yes
    path('sitha/',sitha,name='sitha'),
    path('lavakusa/',lavakusa,name='lavakusa'),
    path('joshna/',joshna,name='joshna'),
    path('lucky/',lucky,name='lucky'),
    path('navyasri/',navyasri,name='navyasri'),

]
