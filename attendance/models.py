from django.db import models

from ordersapp.models import lecture_class
from django.utils import timezone
from datetime import datetime,date

# Create your models here.



# auto_now=True, null
class s_attendance(models.Model):
   subject = models.CharField(max_length=200,null=True)
   f_name = models.CharField(max_length=200,null=True)
   l_name = models.CharField(max_length=200,null=True)
   division = models.CharField(max_length=200,null=True)
   year = models.CharField(max_length=200,null=True)
   attendance = models.CharField(max_length=200,null=True)
   lecture_id = models.CharField(max_length=200,null=True)
   date = models.DateField(auto_now_add=True, null=True)
   time = models.TimeField(auto_now_add=True, null=True)


   def __str__(self):

        return self.subject + " - " + self.division + " - " + str(self.date) 

