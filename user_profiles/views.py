from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from .decorators import unauthenticated_user, allowed_users
from timetable.models import *
from .models import *
import pandas as pd
from algo import generate_passwords
import os
from .forms import ProfilePictureForm

User = get_user_model()
# Create your views here.
@allowed_users(allowed_roles=['teacher','admin'])
def request_to_shift(request):
    if request.method != 'POST':
        return render(request, 'shift_class.html')
    
    src_day = request.POST.get("src_day")
    src_period = request.POST.get("src_period")
    dest_day = request.POST.get("dest_day")
    dest_period = request.POST.get("dest_period")

    messages.info(request, "The request has been sent to the respective faculty. If it is approved, you will be notified.")

    if (dest_period == "1"):
        faculty_receiver = Timetable_IOTCSBT.objects.get(day=dest_day).period1.split()[1].lstrip('(').rstrip(')')
    elif (dest_period == "2"):
        faculty_receiver = Timetable_IOTCSBT.objects.get(day=dest_day).period2.split()[1].lstrip('(').rstrip(')')
    elif (dest_period == "3"):
        faculty_receiver = Timetable_IOTCSBT.objects.get(day=dest_day).period3.split()[1].lstrip('(').rstrip(')')
    elif (dest_period == "4"):
        faculty_receiver = Timetable_IOTCSBT.objects.get(day=dest_day).period4.split()[1].lstrip('(').rstrip(')')
    elif (dest_period == "5"):
        faculty_receiver = Timetable_IOTCSBT.objects.get(day=dest_day).period5.split()[1].lstrip('(').rstrip(')')
    elif (dest_period == "6"):
        faculty_receiver = Timetable_IOTCSBT.objects.get(day=dest_day).period6.split()[1].lstrip('(').rstrip(')')
    elif (dest_period == "7"):
        faculty_receiver = Timetable_IOTCSBT.objects.get(day=dest_day).period7.split()[1].lstrip('(').rstrip(')')

    notification = f"A faculty member has requested a shift in classes. They would like to shift their class that is on {src_day} period {src_period} to {dest_day} period {dest_period}. Do you approve of this shift ?"
    
    Notification.objects.create(
        sender = request.user,
        receiver = faculty_receiver,
        notification = notification
    )

    return redirect('/shift_class/')

@unauthenticated_user
def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = User.objects.filter(username = username)

    if user.exists():
        messages.info(request, 'Username already in use.')
        return redirect('/register/')

    user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username = username,  
    )

    user.set_password(password)
    user.save()

    group = Group.objects.get(name = 'student')
    user.groups.add(group)

    messages.info(request, 'Account created successfully.')

    return redirect('/login/')

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username):
            messages.error(request, 'User does not exist.')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Incorrect password.')
            return redirect('/login/')

        else:
            login(request, user)
            return redirect('/home/')
        
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def new_batch_registration(request):
    cur_path = os.path.dirname(__name__)
    new_path = os.path.relpath('students.xlsx',cur_path)
    try:
        generate_passwords(new_path)
    except ValueError as e:
        pass
    df = pd.read_excel(new_path)
    username = df['Enrolment No'].values.tolist()
    first_name = df['First Name'].values.tolist()
    last_name = df['Last Name'].values.tolist()
    contact_no = df['Contact No'].values.tolist()
    email = df['Email'].values.tolist()
    address = df['Address'].values.tolist()
    stream = df['Stream'].values.tolist()
    days_present = df['Days Present'].values.tolist()
    password = df['Password'].values.tolist()

    for i in range(len(df)):
        user = User.objects.filter(username = username[i])
        if not user.exists():
            user = User.objects.create(
                username = username[i],
                first_name = first_name[i],
                last_name = last_name[i],
                contact_no = contact_no[i],
                email = email[i],
                address = address[i],
                stream = stream[i],
                days_present = days_present[i],
            )

            user.set_password(str(password[i]))
            user.save()

            group = Group.objects.get(name = 'student')
            user.groups.add(group)

    messages.info(request, 'Accounts created successfully.')
    return redirect('/home/')

@login_required(login_url="/login/")
def upload_profile_picture(request,pk):
    user = CustomUserModel.objects.get(id = pk)
    form = ProfilePictureForm(instance=user)

    if request.method == 'POST':  
        form = ProfilePictureForm(request.POST, request.FILES, instance = user)  
        if form.is_valid():  
            form.save() 
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request,"profile_picture.html", {'form': form, 'img_obj': img_object})  
    else:  
        form = ProfilePictureForm()  
  
    return render(request, 'profile_picture.html', {'form': form})

def mark_attendance(request):
    students=[]
    if request.method == "POST":
        stream = request.POST.get("stream")
        students = CustomUserModel.objects.all().filter(groups__name = 'student').filter(stream = stream)
    context = {"students":students,"is_teacher":False}
    if request.user.groups.filter(name = 'teacher').exists():
        context = {"students":students,"is_teacher":True}
    if request.method == "POST" and students:
        attendance_list = request.POST.getlist('mark_as_present')
        print(attendance_list)
        present_students = students.filter(username__in = attendance_list)
        if present_students:
            print(present_students.values())
        # for student in present_students:
        #     student.days_present += 1
        #     student.save()
    return render(request,'mark_attendance.html',context)
    