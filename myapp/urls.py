#from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
     
    path('hello', views.hello,name='hello'),
    path('wlcm/', views.wlcm,name='wlcm'),
]
 
