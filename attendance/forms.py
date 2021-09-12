from django import forms
from django.forms import ModelForm



class attendanceForm(forms.Form):
    subject = forms.CharField(max_length=200)
    f_name = forms.CharField(max_length=200,widget=forms.HiddenInput())
    l_name = forms.CharField(max_length=200,widget=forms.HiddenInput())
    division = forms.CharField(max_length=200,widget=forms.HiddenInput())
    year = forms.CharField(max_length=200,widget=forms.HiddenInput())
    attendance = forms.CharField(max_length=200,widget=forms.HiddenInput())
    lecture_id = forms.CharField(max_length=200,widget=forms.HiddenInput())
    