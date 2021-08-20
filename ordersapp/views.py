from django import forms
from django.db.models.aggregates import Count
from ordersapp.models import lecture_class
from django.shortcuts import render,redirect
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .models import lecture_class 
from django.contrib import messages



# Create your views here.



def home(request):
     return render(request,'index.html',)




def profile(request):
     return render(request,'profile.html',)
     


def classes(request):
     return render(request,'classes.html',)



def teachers(request):
     lectures_create = lecture_class.objects.filter(professor =request.user).order_by('professor')
     print(lectures_create)
     return render(request,'teachers.html', {'lectures_create':lectures_create} )




@login_required(login_url='/accounts/login/')
def lectures(requests,div,year):
          
     all_lecture = lecture_class.objects.all()
     
     
     all_lectures = lecture_class.objects.all().filter(division=div,year=year)
     no_lectures = "No lectures! "     
     return render(requests,'lectures.html',{'all_lectures':all_lectures,'no_lectures':no_lectures})



 
def CreateProduct(requests):
     form1 = ProductForm(requests.POST or None)
     if form1.is_valid():
          data = form1.cleaned_data
          #obj = form1.save(commit=False)
          lecture_class.objects.create(**data)
          form1 = ProductForm()
     return render(requests,"forms.html",{"form": form1})








         
    
