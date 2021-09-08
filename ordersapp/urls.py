from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ordersapp import views



urlpatterns = [
    #path("",views.home,name='index'),
    path("forms/",views.CreateProduct,name='CreateProduct'),
    path("profile/",views.profile,name='profile'),
    path("lectures/<str:div>/<int:year>",views.lectures,name='lectures'),
    path("classes/",views.classes,name='classes'),
    path("teachers/",views.teachers,name='teachers'),
    path("chat/",views.chat,name='chat'),
    path("assignments/",views.assignments,name='assignments'),
    
       
      
    
]

