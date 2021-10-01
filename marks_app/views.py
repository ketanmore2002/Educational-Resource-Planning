from ordersapp.forms import User
from django.shortcuts import redirect, render

from django.contrib.auth.models import User

from marks_app.models import *


# Create your views here.


# def profile(requests):

#      if requests.method == "POST":
#           name = requests.user.username
#           id = requests.user.id
#           table_al = s_attendance.objects.all()
#           table_all = table_al.count
#           table = s_attendance.objects.all().filter(username = name , user_id = id)
#           total = table.count()
#           return render(requests,'attendanceList_students.html',{"table":table,"total":total,"table_all":table_all})
#      else:
#           return render(requests,'profile.html',)



def create_student (request):

    class_teacher_username = request.user.username
    
    ct = class_teacher.objects.all()
    if class_teacher.objects.filter(class_teacher = class_teacher_username).exists():
        
        all = class_teacher.objects.all().filter(class_teacher = class_teacher_username)
        
        division = all[0].division
        year = all[0].year
        return redirect("/all_students/" + division + "/"  + year)

    else:
        
        return redirect("/")       
        
           
def all_students (requests,division,year):

    all_users = User.objects.all()
    class_teacher_username = requests.user.username

    if requests.POST :
        
        class_teacher_name = requests.POST.get('class_teacher_name', None)
        student_name = requests.POST.get('student_name', None)
        prn = requests.POST.get('prn', None)
        roll_number = requests.POST.get('roll_number', None)

        if year == "1" :
            
            first_year_student.objects.create(division = division,year = "1",roll_number = roll_number,prn = prn,student_name = student_name,exam = "CA-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
            first_year_student.objects.create(division = division,year = "1",roll_number = roll_number,prn = prn,student_name = student_name,exam = "CA-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
            first_year_student.objects.create(division = division,year = "1",roll_number = roll_number,prn = prn,student_name = student_name,exam = "SEMETER-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
            first_year_student.objects.create(division = division,year = "1",roll_number = roll_number,prn = prn,student_name = student_name,exam = "SEMETER-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
            return render(requests,'create_student.html',{'all_users':all_users,'division':division,'year':year})
        # elif year == 2 :
        #     second_year_student.objects.create(division = division,year = "2",roll_number = roll_number,student_name = student_name,exam = "CA-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     second_year_student.objects.create(division = division,year = "2",roll_number = roll_number,student_name = student_name,exam = "CA-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     second_year_student.objects.create(division = division,year = "2",roll_number = roll_number,student_name = student_name,exam = "SEMETER-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     second_year_student.objects.create(division = division,year = "2",roll_number = roll_number,student_name = student_name,exam = "SEMETER-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        # elif year == 3 :
        #     third_year_student.objects.create(division = division,year = "3",roll_number = roll_number,student_name = student_name,exam = "CA-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     third_year_student.objects.create(division = division,year = "3",roll_number = roll_number,student_name = student_name,exam = "CA-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     third_year_student.objects.create(division = division,year = "3",roll_number = roll_number,student_name = student_name,exam = "SEMETER-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     third_year_student.objects.create(division = division,year = "3",roll_number = roll_number,student_name = student_name,exam = "SEMETER-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        # elif year == 4 :
        #     fourth_year_student.objects.create(division = division,year = "4",roll_number = roll_number,student_name = student_name,exam = "CA-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     fourth_year_student.objects.create(division = division,year = "4",roll_number = roll_number,student_name = student_name,exam = "CA-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     fourth_year_student.objects.create(division = division,year = "4",roll_number = roll_number,student_name = student_name,exam = "SEMETER-1",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)
        #     fourth_year_student.objects.create(division = division,year = "4",roll_number = roll_number,student_name = student_name,exam = "SEMETER-2",class_teacher_name = class_teacher_name,class_teacher_username = class_teacher_username)

    else:
        return render(requests,'create_student.html',{'all_users':all_users,'division':division,'year':year})
    
    return render(requests,'create_student.html',{'all_users':all_users,'division':division,'year':year})

    
    

def ca1 (requests):
   
    class_teacher_username = requests.user.username

    if class_teacher.objects.filter(class_teacher = class_teacher_username).exists():
        
        all = class_teacher.objects.all().filter(class_teacher = class_teacher_username)
        print(all)
        division = all[0].division
        year = all[0].year
        
    else:
        
        return redirect("/teachers_profile")       
    
    if year == "1" :
            table = first_year_student.objects.all().filter(exam = "CA-1",division = division,year = "1",class_teacher_username = class_teacher_username).order_by('roll_number')
            exam = "CA-1"
            return render(requests,'marks_table.html',{'division':division,'year':year,'table':table,'exam':exam})

    # # elif year == "2" :
    # #         marks = second_year_student.objects.all().filter(division = division,year = "2",class_teacher_username = class_teacher_username)
    #           return render(requests,'marks.html',{'division':division,'year':year,'marks':marks})

    # # elif year == "3" :
    # #         marks = third_year_student.objects.all().filter(division = division,year = "3",class_teacher_username = class_teacher_username)
    #           return render(requests,'marks.html',{'division':division,'year':year,'marks':marks})

    # # elif year == "4" :
    # #         marks = fourth_year_student.objects.all().filter(division = division,year = "4",class_teacher_username = class_teacher_username)
    #           return render(requests,'marks.html',{'division':division,'year':year,'marks':marks})

    
    











 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 # physics = requests.POST.get('physics', None)
        # chemistry = requests.POST.get('chemistry', None)
        # maths_1 = requests.POST.get('maths_1', None)
        # maths_2 = requests.POST.get('maths_2', None)
        # pic = requests.POST.get('pic', None)
        # cs = requests.POST.get('cs', None)
        # machanics = requests.POST.get('machanics', None)
        # graphics = requests.POST.get('graphics', None)
        # bce = requests.POST.get('bce', None)
        # eee = requests.POST.get('eee', None)
        # exam = requests.POST.get('f_name', None)
        # marks = requests.POST.get('marks', None)
