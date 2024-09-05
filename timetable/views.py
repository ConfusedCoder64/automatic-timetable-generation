from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
import random
from .models import *
from user_profiles.models import Notification
from algo import check, dict_sum, replace_elective, replace_labs
from user_profiles.decorators import allowed_users, admin_only
from django.http import HttpResponse

# Create your views here.
@login_required(login_url = "/login/")    
def home_page(request):
    if(Notification.objects.all().count() > 0):
        current_notif = Notification.objects.all().order_by('-id')[:1][0]
        context = {"flag1":True, "flag2":False}
        if (request.user.username == current_notif.receiver) and (current_notif.viewed == 0):
            messages.info(request, current_notif.notification)

            if (request.method == 'POST'):
                choice = request.POST.get("choice")
                if (choice == "Yes"):
                    current_notif.approved = True
                    current_notif.save()

                    src_day = current_notif.notification.split()[19]
                    src_period = current_notif.notification.split()[21]
                    dest_day = current_notif.notification.split()[23]
                    dest_period = current_notif.notification.split()[25].rstrip('.')

                    if (src_period == "1"):
                        src_class = Timetable_IOTCSBT.objects.get(day=src_day).period1
                    elif (src_period == "2"):
                        src_class = Timetable_IOTCSBT.objects.get(day=src_day).period2
                    elif (src_period == "3"):
                        src_class = Timetable_IOTCSBT.objects.get(day=src_day).period3
                    elif (src_period == "4"):
                        src_class = Timetable_IOTCSBT.objects.get(day=src_day).period4
                    elif (src_period == "5"):
                        src_class = Timetable_IOTCSBT.objects.get(day=src_day).period5
                    elif (src_period == "6"):
                        src_class = Timetable_IOTCSBT.objects.get(day=src_day).period6
                    elif (src_period == "7"):
                        src_class = Timetable_IOTCSBT.objects.get(day=src_day).period7

                    if (dest_period == "1"):
                        dest_class = Timetable_IOTCSBT.objects.get(day=dest_day).period1
                        obj = Timetable_IOTCSBT.objects.get(day=dest_day)
                        obj.period1 = src_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=dest_day)
                        obj.period1 = src_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=dest_day)
                        obj.period1 = src_class
                        obj.save()
                    elif (dest_period == "2"):
                        dest_class = Timetable_IOTCSBT.objects.get(day=dest_day).period2
                        obj = Timetable_IOTCSBT.objects.get(day=dest_day)
                        obj.period2 = src_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=dest_day)
                        obj.period2 = src_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=dest_day)
                        obj.period2 = src_class
                        obj.save()
                    elif (dest_period == "3"):
                        dest_class = Timetable_IOTCSBT.objects.get(day=dest_day).period3
                        obj = Timetable_IOTCSBT.objects.get(day=dest_day)
                        obj.period3 = src_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=dest_day)
                        obj.period3 = src_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=dest_day)
                        obj.period3 = src_class
                        obj.save()
                    elif (dest_period == "4"):
                        dest_class = Timetable_IOTCSBT.objects.get(day=dest_day).period4
                        obj = Timetable_IOTCSBT.objects.get(day=dest_day)
                        obj.period4 = src_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=dest_day)
                        obj.period4 = src_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=dest_day)
                        obj.period4 = src_class
                        obj.save()
                    elif (dest_period == "5"):
                        dest_class = Timetable_IOTCSBT.objects.get(day=dest_day).period5
                        obj = Timetable_IOTCSBT.objects.get(day=dest_day)
                        obj.period5 = src_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=dest_day)
                        obj.period5 = src_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=dest_day)
                        obj.period5 = src_class
                        obj.save()
                    elif (dest_period == "6"):
                        dest_class = Timetable_IOTCSBT.objects.get(day=dest_day).period6
                        obj = Timetable_IOTCSBT.objects.get(day=dest_day)
                        obj.period6 = src_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=dest_day)
                        obj.period6 = src_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=dest_day)
                        obj.period6 = src_class
                        obj.save()
                    elif (dest_period == "7"):
                        dest_class = Timetable_IOTCSBT.objects.get(day=dest_day).period7
                        obj = Timetable_IOTCSBT.objects.get(day=dest_day)
                        obj.period7 = src_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=dest_day)
                        obj.period7 = src_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=dest_day)
                        obj.period7 = src_class
                        obj.save()


                    if (src_period == "1"):
                        obj = Timetable_IOTCSBT.objects.get(day=src_day)
                        obj.period1 = dest_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=src_day)
                        obj.period1 = dest_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=src_day)
                        obj.period1 = dest_class
                        obj.save()
                    elif (src_period == "2"):
                        obj = Timetable_IOTCSBT.objects.get(day=src_day)
                        obj.period2 = dest_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=src_day)
                        obj.period2 = dest_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=src_day)
                        obj.period2 = dest_class
                        obj.save()
                    elif (src_period == "3"):
                        obj = Timetable_IOTCSBT.objects.get(day=src_day)
                        obj.period3 = dest_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=src_day)
                        obj.period3 = dest_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=src_day)
                        obj.period3 = dest_class
                        obj.save()
                    elif (src_period == "4"):
                        obj = Timetable_IOTCSBT.objects.get(day=src_day)
                        obj.period4 = dest_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=src_day)
                        obj.period4 = dest_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=src_day)
                        obj.period4 = dest_class
                        obj.save()
                    elif (src_period == "5"):
                        obj = Timetable_IOTCSBT.objects.get(day=src_day)
                        obj.period5 = dest_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=src_day)
                        obj.period5 = dest_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=src_day)
                        obj.period5 = dest_class
                        obj.save()
                    elif (src_period == "6"):
                        obj = Timetable_IOTCSBT.objects.get(day=src_day)
                        obj.period6 = dest_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=src_day)
                        obj.period6 = dest_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=src_day)
                        obj.period6 = dest_class
                        obj.save()
                    elif (src_period == "7"):
                        obj = Timetable_IOTCSBT.objects.get(day=src_day)
                        obj.period7 = dest_class
                        obj.save()
                        obj = Timetable_IOT.objects.get(day=src_day)
                        obj.period7 = dest_class
                        obj.save()
                        obj = Timetable_IT.objects.get(day=src_day)
                        obj.period7 = dest_class
                        obj.save()
                    
                current_notif.viewed = True
                current_notif.save()
            
        elif (request.user.username == current_notif.sender) and (current_notif.acknowledged == False):
            context = {"flag1":False, "flag2":True}
            if (current_notif.approved == 1):
                messages.info(request,'Your request has been approved, it will be reflected in the timetable shortly.')
                
            elif (current_notif.approved == 0) and (current_notif.viewed == 1):
                messages.info(request,'Your request has been rejected.')

            if (request.method == "POST"):
                current_notif.acknowledged = True
                current_notif.save()

        return render(request,'home_page.html',context)
    return render(request,'home_page.html')

def create_timetable(request):
    try:  
        if(Timetable_IOTCSBT.objects.filter(day = "Monday").count() == 0):
            data = pd.read_excel("data.xlsx")
            subjects = data['Subject'].values.tolist()
            faculty = data['Faculty'].values.tolist()
            no_of_classes = data['No. of classes'].values.tolist()
            temp = []

            for i in range(len(faculty[:24])):
                temp.append(f"{subjects[i]} ({faculty[i]})")
            classes = dict(zip(temp,no_of_classes[:24]))
            temp.clear()
            for i in range(len(faculty[:24]),len(faculty)):
                temp.append(f"{subjects[i]} ({faculty[i]})")
            labs = dict(zip(temp,no_of_classes[24:]))
            
            week=[]
            day=[]
            while dict_sum(classes) > 0:
                for value in classes.values():
                    if value > 0:
                        val = check(classes)
                        classes[val] -= 1
                        day.append(val)
                        if len(day) % 5 == 0 or dict_sum(classes) == 0:
                            rand_val = random.randint(0,5)
                            val_lab = check(labs)
                            labs[val_lab] -= 2
                            day.insert(rand_val,val_lab)
                            day.insert(rand_val+1,val_lab)
                            week.append(day)
                            day = []
            
            labs_record = []
            if (len(labs_record) > 5):
                labs_record = labs_record[:5]
                
            weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
            for i in range(5):
                Timetable_IOTCSBT.objects.create(
                    day = weekdays[i],
                    period1 = week[i][0],
                    period2 = week[i][1],
                    period3 = week[i][2],
                    period4 = week[i][3],
                    period5 = week[i][4],
                    period6 = week[i][5],
                    period7 = week[i][6],
                )

            labs = dict(zip(temp,no_of_classes[24:]))
            week = replace_elective(week,"IOT")
            week = replace_labs(week, labs, labs_record)
            for i in range(5):
                Timetable_IOT.objects.create(
                    day = weekdays[i],
                    period1 = week[i][0],
                    period2 = week[i][1],
                    period3 = week[i][2],
                    period4 = week[i][3],
                    period5 = week[i][4],
                    period6 = week[i][5],
                    period7 = week[i][6],
                )

            if (len(labs_record) > 5):
                labs_record = labs_record[:5]
            labs = dict(zip(temp,no_of_classes[24:]))
            week = replace_elective(week,"IT")
            week = replace_labs(week, labs, labs_record)
            for i in range(5):
                Timetable_IT.objects.create(
                    day = weekdays[i],
                    period1 = week[i][0],
                    period2 = week[i][1],
                    period3 = week[i][2],
                    period4 = week[i][3],
                    period5 = week[i][4],
                    period6 = week[i][5],
                    period7 = week[i][6],
                )
            
            return render(request,'timetable_generation_successful.html')
    except IndexError as e:
        return render(request,"error.html")
    return redirect('/home/')

@login_required(login_url = "/login/")    
def display_timetable_IOTCSBT(request):  
    queryset = Timetable_IOTCSBT.objects.all()
    context = {'days':queryset,'is_teacher':False}
    user = request.user
    if user.groups.filter(name="teacher").exists():
        context = {'days':queryset,'is_teacher':True}
    return render(request,'timetable_IOTCSBT.html',context)

@login_required(login_url = "/login/")    
def display_timetable_IOT(request):  
    queryset = Timetable_IOT.objects.all()
    context = {'days':queryset,'is_teacher':False}
    user = request.user
    if user.groups.filter(name="teacher").exists():
        context = {'days':queryset,'is_teacher':True}
    return render(request,'timetable_IOT.html',context)

@login_required(login_url = "/login/")    
def display_timetable_IT(request):  
    queryset = Timetable_IT.objects.all()
    context = {'days':queryset,'is_teacher':False}
    user = request.user
    if user.groups.filter(name="teacher").exists():
        context = {'days':queryset,'is_teacher':True}
    return render(request,'timetable_IT.html',context)

def delete_timetable(request):
    queryset = Timetable_IOTCSBT.objects.all()
    queryset.delete()
    queryset = Timetable_IOT.objects.all()
    queryset.delete()
    queryset = Timetable_IT.objects.all()
    queryset.delete()
    return redirect('/home/')

    

