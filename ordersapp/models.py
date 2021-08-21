from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
 

class lecture_class(models.Model):
     subject = models.CharField(max_length=2000)
     professor = models.CharField(max_length=20000)
     time = models.TimeField()
     division = models.CharField(max_length=20000, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')] )
     year = models.CharField(max_length=20000,choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')])
     link =  models.CharField(max_length=20000)

     def __str__(self):

        return self.professor + "-" +self.subject + "-" +self.year + "-" +(self.division).upper()  


