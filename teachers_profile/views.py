from django.shortcuts import render,redirect

from attendance.models import s_attendance
from ordersapp.models import lecture_class

from django.contrib.auth.models import User

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/accounts/login/')
@staff_member_required(login_url='/')
def teachers_profile(request):

    if request.method == 'POST':
        subject = request.POST.get('subject', None)
        division = request.POST.get('division', None)
        year = request.POST.get('year', None)
        date = request.POST.get('attendance_date', None)
        return redirect('/attendanceList/'+division+'/'+year+'/'+date+'/'+subject+'/')
    else:
        pass
       
    return render(request,'teachers_profile.html',)





def lectures_list(request):

    name = request.user.username
    table = lecture_class.objects.all().filter(professor = name)
    lecture_id = request.POST.get('lecture_id', None)
    lecture_class.objects.all().filter(lecture_id = lecture_id).delete()
    

    return render(request,'lectures_list.html',{'table':table})






def attendanceList(request,divi,ear,sub,date):

    # print("Namne 2",divi,ear,sub)
    
    table = s_attendance.objects.all().filter(division = divi,year = ear,subject = sub,date = date)

    total = table.count()

    return render(request,'attendanceList.html',{"table":table,"total":total})






def create_lectures(request):

    if request.method == 'POST':
        subject = request.POST.get('subject', None)
        division = request.POST.get('division', None)
        professor  = request.POST.get('professor', None)
        year = request.POST.get('year', None)
        link = request.POST.get('link', None)
        date = request.POST.get('date', None)
        time = request.POST.get('time', None)
        status = request.POST.get('status', None)
        print("Namne",subject,division,professor,year,date,time,link)
        lecture_class.objects.create(subject = subject,division = division,professor = professor,year = year,link = link,date = date,time = time,status = status)
    else:
        pass

    return render(request,'create_lectures.html')





def attendanceListid(request,id):

    # print("Namne 2",divi,ear,sub)
    
    table = s_attendance.objects.all().filter(lecture_id = id)

    total = table.count()

    return render(request,'attendanceList.html',{"table":table,"total":total})







def lectures_list_status(requests):

    name = requests.user.username
    table = lecture_class.objects.all().filter(professor = name)
    if requests.method == "POST":
     ids = requests.POST.get('id', None)
     lecture_class.objects.all().filter(lecture_id = ids).update(status = "unpublished")
     
     
    else:
        return render(requests,'lectures_status.html',{'table':table})

    return render(requests,'lectures_status.html',{'table':table})










def forms_lectures(requests,uuid):

    all_lectures = lecture_class.objects.all().filter(lecture_id=uuid)

    table = s_attendance.objects.all().filter(lecture_id = uuid)

    total = table.count()

    if requests.method == "POST":  
     f_name = requests.POST.get('f_name', None)
     l_name = requests.POST.get('l_name', None)
     attendance = requests.POST.get('attendance', None)
     division = requests.POST.get('division', None)
     year = requests.POST.get('year', None)
     subject = requests.POST.get('subject', None)
     lecture_id = requests.POST.get('lecture_id', None)

     if attendance != None and f_name != None and l_name != None and division != None and subject != None and year != None:
          s_attendance.objects.create(attendance =attendance,f_name = f_name,l_name = l_name, division = division,subject = subject,year = year,lecture_id=lecture_id)
          print("name :" ,attendance,f_name,l_name,division,year)
     else:
          pass 
    
    else:
        return render(requests,'forms_lectures.html',{"all_lectures":all_lectures,"total":total})
        
     
    return render(requests,'forms_lectures.html',{"all_lectures":all_lectures,"total":total})