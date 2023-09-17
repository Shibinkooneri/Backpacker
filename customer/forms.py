from django import forms
from .models import UserUploads,TravelInvites,Profilepictures

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserUploadsForm(forms.ModelForm):
    class Meta:
        model=UserUploads
        fields=['img','location']
    
class UserInviteForm(forms.ModelForm):
    class Meta:
        model=TravelInvites
        fields=['Destination','Location','Description']

class PropicForm(forms.ModelForm):
    class Meta:
        model=Profilepictures
        fields=['Pic','Homeloc']

class ProfileForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']