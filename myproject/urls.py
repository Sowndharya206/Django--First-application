"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mymessage/',views.mymessage),
    path('car/',views.index),  
    path('index2/',views.index1),
    path('show/',views.shows),
    path('index3/',views.index3),
    path('img/',views.img),
    path('jas/',views.jas1),
    path('colr/',views.colo),
    path('but/',views.wrks),
    path('buttons/',views.buttons),
    path('but/',views.wrke),
    path('image/',views.image),
    path('csv/',views.getfile),
    path('did/',views.done),
    path('pdf',views.getpdf), 
]
