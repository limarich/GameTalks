from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.forms import LoginForm, SignupForm

def login(request):
    login_form = LoginForm()
    signup_form = SignupForm()
    return render(request, 'pages/login.html', {'login_form': login_form, 'signup_form': signup_form})

@login_required
def profile(request):
    return render(request, 'pages/profile.html',{});
