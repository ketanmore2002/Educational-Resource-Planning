from django.contrib import admin

from .models import lecture_class,class_assignments

# Register your models here.

admin.site.register(lecture_class)
admin.site.register(class_assignments)


