from django import forms
from django.contrib.auth import get_user_model



class ProductForm(forms.Form):
     title = forms.CharField(max_length=200)
     price = forms.IntegerField()




User =get_user_model()

class RegisterForm(forms.Form):
     username = forms.CharField(max_length=200)
     password = forms.CharField(max_length=200)
     email = forms.EmailField(max_length=200)




