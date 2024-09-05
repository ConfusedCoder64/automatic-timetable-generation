"""
URL configuration for timetable_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from timetable.views import *
from user_profiles.views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name = "home_page"),
    path('timetable_IOTCSBT/', display_timetable_IOTCSBT, name = "display_timetable_IOTCSBT"),
    path('timetable_IOT/', display_timetable_IOT, name = "display_timetable_IOT"),
    path('timetable_IT/', display_timetable_IT, name = "display_timetable_IT"),
    path('create_timetable/', create_timetable, name = "create_timetable"),
    path('delete_timetable/', delete_timetable, name = "delete_timetable"),
    path('register/', register, name = "register"),
    path('login/', login_page, name = "login_page"),
    path('logout/', logout_page, name = "logout_page"),
    path('shift_class/', request_to_shift, name = "shift_class"),
    path('new_batch_registration/', new_batch_registration, name = "new_batch_registration"),
    path('upload_profile_picture/<str:pk>/',upload_profile_picture,name="upload_profile_picture"),
    path('mark_attendance/', mark_attendance, name = "mark_attendance")
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  