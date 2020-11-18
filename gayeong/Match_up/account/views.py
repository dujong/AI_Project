from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages




# Create your views here.
def main(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    context = {
        'username' 
    }

    return render(request, 'main.html')

def log_in(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    if request.method == "POST":
        user_name = request.POST['user_id']
        password = request.POST['password']
        user = auth.authenticate(request, username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            
            return redirect('account:main')

        else:
            print("인증실패")
    return render(request, 'log_in.html')

def log_out(request):
    auth.logout(request)

    return redirect('account:log_in')

    
def sign_up(request):
    error = "회원가입이 되지 않음"
    if request.method == "POST":
        form = SignupForm(request.POST)
        if request.POST["password1"]==request.POST["password2"]:
            error = "통과 1"
            print(form.errors)
            if form.is_valid():
                error = "통과 2"
                user = User.objects.create_user(
                    username=request.POST.get("user_id"),
                    password=request.POST.get("password1")
                )
                profile = Profile(
                    user=user,
                    user_name=form.cleaned_data.get('user_name'),
                    email=form.cleaned_data.get('email'), 
                    phone=form.cleaned_data.get('phone'),
                    f_region = form.cleaned_data.get('f_region'),

                )
                profile.save()
                auth.login(request, user)
                return redirect('/')
        else:
            error = "비밀번호를 다시 확인해주세요!"
            
    else:
        if request.user.is_authenticated:
            return redirect('/')

        form = SignupForm()

    return render(request, "sign_up.html", {"form":form, "error":error,})


def my_page(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        my_profile = Profile.objects.get(user__username=request.user)
        return render(request, 'my_page.html',{'username':username, 'my_profile' : my_profile,})
    else:
        return redirect('/my_page')
