from django import forms
from django.contrib.auth.models import User
from . import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = models.UserInfo
        fields = ('fb_link', 'profile_pic')
