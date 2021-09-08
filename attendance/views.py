from django.shortcuts import render

from django.contrib.auth.models import User


# Create your views here.




from django_tables2 import SingleTableView

from .models import s_attendance
from .tables import s_attendanceTable


class s_attendanceTable(SingleTableView):
    model = s_attendance
    table_class = s_attendanceTable
    template_name = 'tables.html'




# def attendanceList(request):

#      table = s_attendance.objects.all()

#      return render(request,'attendanceList.html',{"table":table})