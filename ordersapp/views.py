from django import forms
from django.db.models.aggregates import Count
from ordersapp.models import lecture_class
from django.shortcuts import render,redirect
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import lecture_class , class_assignments
from attendance.models import s_attendance
from django.contrib import messages
from attendance.forms import attendanceForm




# Create your views here.



def home(requests):

     return render(requests,'index.html',)




def profile(requests):

     # if requests.method == "POST":
     #      name = requests.user.username
     #      id = requests.user.id
     #      table_al = s_attendance.objects.all()
     #      table_all = table_al.count
     #      table = s_attendance.objects.all().filter(username = name , user_id = id)
     #      total = table.count()
     #      return render(requests,'attendanceList_students.html',{"table":table,"total":total,"table_all":table_all})
     # else:
     return redirect ("teachers_profile")
     
    
     


def classes(request):
     all_chats= lecture_class.objects.all()
     return render(request,'classes.html',{'all_chats':all_chats})



def chat(request):
     return render(request,'chat.html',)



def teachers(request):
     lectures_create = lecture_class.objects.filter(professor =request.user).order_by('professor')
     print(lectures_create)
     return render(request,'teachers.html', {'lectures_create':lectures_create} )




@login_required(login_url='/accounts/login/')
def lectures(request,div,year):
          
     all_lectures = lecture_class.objects.all().filter(division=div,year=year)
     count =  all_lectures.count()   
     return render(request,'lectures.html',{'all_lectures':all_lectures,'div':div,'year':year,'count':count})





@login_required(login_url='/accounts/login/')
def assignments(request):

     all_assignments = class_assignments.objects.all()
 
     return render(request,'assignments.html',{'all_assignments':all_assignments})





































def CreateProduct(requests):
     form1 = ProductForm(requests.POST or None)
     if form1.is_valid():
          data = form1.cleaned_data
          #obj = form1.save(commit=False)
          lecture_class.objects.create(**data)
          form1 = ProductForm()
     return render(requests,"forms.html",{"form": form1})








         
    
