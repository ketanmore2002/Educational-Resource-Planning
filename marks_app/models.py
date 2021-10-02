from django.contrib.auth.models import User
from django.db import models


import uuid

from django.db.models.deletion import SET_NULL

# Create your models here.

class subject (models.Model):
   subject = models.CharField(max_length=20000,null=True)

   def __str__(self):
        return self.subject


class exams (models.Model):
   exam = models.CharField(max_length=20000,null=True)
   

   def __str__(self):
        return self.exam


class student (models.Model):
   name = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
   prn = models.CharField(max_length=20000,null=True)

   # def __str__(self):
   #      return self.name 
   

class student_main (models.Model):
   class_teacher_name = models.CharField(max_length=20000,null=True)
   class_teacher_username = models.CharField(max_length=20000,null=True)
   student = models.CharField(max_length=20000,null=True)
   division = models.CharField(max_length=20000, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')] ,null=True)
   year = models.CharField(max_length=20000,choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')],null=True)
   subject = models.CharField(max_length=20000,null=True)
   student_code = models.UUIDField(default = uuid.uuid4, editable = False,null=True)
   exam = models.CharField(max_length=20000,null=True)
   marks = models.IntegerField(null=True)

   def __str__(self):
        return self.student 
   
   


class class_teacher (models.Model):
   class_teacher = models.CharField(max_length=20000,null=True)
   division = models.CharField(max_length=20000, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')] ,null=True)
   year = models.CharField(max_length=20000,choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')],null=True)





class first_year_student (models.Model):
   class_teacher_name = models.CharField(max_length=20000,null=True)
   class_teacher_username = models.CharField(max_length=20000,null=True)
   student_name = models.CharField(max_length=20000,null=True)
   division = models.CharField(max_length=20000, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')] ,null=True)
   prn = models.IntegerField(null=True)
   roll_number = models.IntegerField(null=True)
   physics = models.CharField(max_length=20000,null=True)
   year = models.CharField(max_length=20000,default="1",null=True)
   chemistry = models.CharField(max_length=20000,null=True)
   maths_1 = models.CharField(max_length=20000,null=True)
   maths_2 = models.CharField(max_length=20000,null=True)
   pic = models.CharField(max_length=20000,null=True)
   cs = models.CharField(max_length=20000,null=True)
   machanics = models.CharField(max_length=20000,null=True)
   graphics = models.CharField(max_length=20000,null=True)
   bce = models.CharField(max_length=20000,null=True)
   eee = models.CharField(max_length=20000,null=True)
   student_code = models.UUIDField(default = uuid.uuid4, editable = False,null=True,unique=True)
   exam = models.CharField(max_length=20000,null=True)
   marks = models.IntegerField(null=True)

   def __str__(self):
        return self.student_name