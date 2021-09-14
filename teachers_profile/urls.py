from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from teachers_profile import views

from .views import *


urlpatterns = [
    #path("",views.home,name='index'),
    path("teachers_profile/",views.teachers_profile,name='teachers_profile'),
    path("attendanceList/<str:divi>/<str:ear>/<str:date>/<str:sub>/",views.attendanceList,name='attendanceList'),
    path("attendanceList_manual/<str:division>/<str:year>/<str:date>/<str:name>/",views.attendanceList_manual,name='attendanceList_manual'),
    path("attendanceListid/<str:id>/",views.attendanceListid,name='attendanceListid'),
    path("lectures_list/",views.lectures_list,name='lectures_list'),
    path("lectures_list_status/",views.lectures_list_status,name='lectures_list_status'),
    path("create_lectures/",views.create_lectures,name='create_lectures'),
    path("forms_lectures/<str:uuid>/",views.forms_lectures,name='forms_lectures'),
    path("unpublish_lecture/<str:ids>/",views.unpublish_lecture,name='unpublish_lecture'),
    path("lectures_delete/<str:ids>/",views.lectures_delete,name='lectures_delete'),
    path("redict_lecture/<str:url>/",views.redict_lecture,name='redict_lecture'),
     
   
]
