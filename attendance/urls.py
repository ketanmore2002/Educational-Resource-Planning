from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from attendance import views

from attendance.views import s_attendanceTable


urlpatterns = [
    #path("",views.home,name='index'),
    path("tables/", s_attendanceTable.as_view()),
    
     
   
]
