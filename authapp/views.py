from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserInfo

# Create your views here.
@login_required
def home(request):
    dict = {}
    if request.user.is_authenticated:
        currentUser = request.user
        userId = currentUser.id
        userInfoA = User.objects.get(pk=userId)
        userInfoB = UserInfo.objects.get(user__pk=userId)
        dict={
            'userInfoA':userInfoA,
            'userInfoB':userInfoB,
        }

        # print(currentUser.username)

    return render(request, 'index.html', context=dict)

def reg(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        user_info_form = forms.UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()
            
            registered = True

    else:
        user_form = forms.UserForm()
        user_info_form = forms.UserInfoForm()
    dict = {
        'user_form':user_form,
        'user_info_form':user_info_form,
        'registered':registered,
    }
    return render(request, 'reg.html', context=dict)

def login_page(request):
    return render(request, 'login.html')


def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("User is not active")
            
        else:
            return HttpResponse("Login Details are wrong")

    else:
        return render(request, 'login.html', context={})

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userlogin'))
