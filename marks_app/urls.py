from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from marks_app import views



urlpatterns = [
    #path("",views.home,name='index'),
    # path("forms/",views.CreateProduct,name='CreateProduct'),
    path("create_student/",views.create_student,name='create_student'),
    path("all_students/<str:division>/<str:year>",views.all_students,name ='all_students'),     
    path("ca1/",views.ca1,name='ca1'),
       
      
    
]

