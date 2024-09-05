from django.db import models  
from django.forms import fields  
from .models import CustomUserModel  
from django import forms  
  
  
class ProfilePictureForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = CustomUserModel   
        fields = ('profile_picture',)