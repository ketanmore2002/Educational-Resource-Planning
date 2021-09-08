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






# Create your views here.



def home(request):
     return render(request,'index.html',)




def profile(request):
     return render(request,'profile.html',)
     


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
def lectures(requests,div,year):
     
     all_lectures = lecture_class.objects.all().filter(division=div,year=year)
     render(requests,'lectures.html',{'all_lectures':all_lectures})


     f_name = requests.POST.get('f_name', None)
     l_name = requests.POST.get('l_name', None)
     attendance = requests.POST.get('attendance', None)
     division = requests.POST.get('division', None)
     year = requests.POST.get('year', None)
     subject = requests.POST.get('subject', None)
     lecture_id = requests.POST.get('lecture_id', None)
        
   
     if attendance != None and f_name != None and l_name != None and division != None and subject != None and year != None:
          s_attendance.objects.create(attendance =attendance,f_name = f_name,l_name = l_name, division = division,subject = subject,year = year,lecture_id=lecture_id)
          print("name :" ,attendance,f_name,l_name,division,year)
     else:
          pass    
          
     return render(requests,'lectures.html',{'all_lectures':all_lectures})





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








         
    
