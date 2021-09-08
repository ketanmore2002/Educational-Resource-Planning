from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime,date
# Create your models here.
 

class lecture_class(models.Model):
     subject = models.CharField(max_length=2000)
     professor = models.CharField(max_length=20000)
     time = models.TimeField()
     division = models.CharField(max_length=20000, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')] )
     year = models.CharField(max_length=2000,choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')])
     link =  models.CharField(max_length=20000)
     date = models.DateField(auto_now_add=True, blank=True)
     status =  models.CharField(max_length=20000, null = True)

     def __str__(self):

        return self.professor + " - " + self.subject + " - " + (self.division).upper() + " - " + self.year   



class class_assignments(models.Model):
   topic = models.CharField(max_length=20000)
   professor = models.CharField(max_length=20000)
   subject = models.CharField(max_length=2000)
   date = models.DateField(auto_now_add=False, blank=True)
   division = models.CharField(max_length=20000, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')] )
   year = models.CharField(max_length=20000,choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')])
   link =  models.CharField(max_length=20000)
   

   def __str__(self):
      return self.topic + " - "  +  self.professor + " - " + self.subject + " - " + (self.division).upper() + " - " + self.year   

   

       
        


