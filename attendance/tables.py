import django_tables2 as tables
from .models import s_attendance

class s_attendanceTable(tables.Table):
    class Meta:
        model = s_attendance
        template_name = "tables.html"
        sequence = ("f_name","date","l_name","division","attendance","subject")



# class s_attendanceTable(tables.Table):
#     class Meta:
#         model = s_attendance
       