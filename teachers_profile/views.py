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

    name = request.user.username

    if request.method == 'POST':
        
        division = request.POST.get('division', None)
        year = request.POST.get('year', None)
        date = request.POST.get('attendance_date', None)
        return redirect('/attendanceList_manual/'+division+'/'+year+'/'+date+'/'+name+'/')
    
    else:
        return render(request,'teachers_profile.html',)
       
    # return render(request,'teachers_profile.html',)




def attendanceList_manual(requests,division,year,date,name):
    
     table = lecture_class.objects.all().filter(division = division,year = year,professor = name,date = date)
    
     name = requests.user.username
   
     return render(requests,'attendanceList_manual.html',{'table':table})





@login_required(login_url='/accounts/login/')
@staff_member_required(login_url='/')
def lectures_list(request):

    name = request.user.username
    table = lecture_class.objects.all().filter(professor = name)
       

    return render(request,'lectures_list.html',{'table':table})






def attendanceList(request,divi,ear,sub,date):

    # print("Namne 2",divi,ear,sub)
    
    table = s_attendance.objects.all().filter(division = divi,year = ear,subject = sub,date = date)

    total = table.count()

    return render(request,'attendanceList.html',{"table":table,"total":total})





@login_required(login_url='/accounts/login/')
@staff_member_required(login_url='/')
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
        delete_status = request.POST.get('delete_status', None)
        print("Namne",subject,division,professor,year,date,time,link)
        lecture_class.objects.create(subject = subject,division = division,professor = professor,year = year,link = link,date = date,time = time,status = status,delete_status = delete_status)
    else:
        pass

    return render(request,'create_lectures.html')




@login_required(login_url='/accounts/login/')
@staff_member_required(login_url='/')
def attendanceListid(request,id):

    # print("Namne 2",divi,ear,sub)
    
    table = s_attendance.objects.all().filter(lecture_id = id)

    total = table.count()

    return render(request,'attendanceList.html',{"table":table,"total":total})






@login_required(login_url='/accounts/login/')
@staff_member_required(login_url='/')
def lectures_list_status(requests):

    name = requests.user.username
    
    table = lecture_class.objects.all().filter(professor = name)
    
    return render(requests,'lectures_status.html',{'table':table})









@login_required(login_url='/accounts/login/')

def forms_lectures(requests,uuid):

    all_lectures = lecture_class.objects.all().filter(lecture_id=uuid)

    table = s_attendance.objects.all().filter(lecture_id = uuid)

    total = table.count()

    if requests.method == "POST":  
     f_name = requests.POST.get('f_name', None)
     l_name = requests.POST.get('l_name', None)
     username = requests.POST.get('username', None)
     user_id = requests.POST.get('user_id', None)
     attendance = requests.POST.get('attendance', None)
     division = requests.POST.get('division', None)
     year = requests.POST.get('year', None)
     subject = requests.POST.get('subject', None)
     lecture_id = requests.POST.get('lecture_id', None)
     url = requests.POST.get('url', None)

     

     if attendance != None and f_name != None and l_name != None and division != None and subject != None and year != None and username != None and user_id != None:
          s_attendance.objects.create(attendance =attendance,f_name = f_name,l_name = l_name, division = division,subject = subject,year = year,lecture_id=lecture_id,user_id = user_id,username = username)
          print("name :" ,attendance,f_name,l_name,division,year)
         
          return redirect("https://"+ str(url))
          
          
     else:
          pass 
    
    else:
        return render(requests,'forms_lectures.html',{"all_lectures":all_lectures,"total":total})
        
     
    return render(requests,'forms_lectures.html',{"all_lectures":all_lectures,"total":total})




def unpublish_lecture(requests,ids):
    
     lecture_class.objects.all().filter(lecture_id = ids).update(status = "unpublished")
    
     name = requests.user.username

     table = lecture_class.objects.all().filter(professor = name)
    
     return redirect('/lectures_list_status/',{'table':table})
     
     
    

def lectures_delete(requests,ids):
    
     lecture_class.objects.all().filter(lecture_id = ids).update(delete_status = "deleted")

     lecture_class.objects.all().filter(lecture_id = ids).update(status = "unpublished")
    
     name = requests.user.username

     table = lecture_class.objects.all().filter(professor = name)
    
     return redirect('/lectures_list/',{'table':table})      

    

def redict_lecture(requests,url):

    return redirect("//"+ url)