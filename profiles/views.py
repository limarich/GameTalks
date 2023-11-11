from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login(request):
    # return render(request, 'pages/login.html', {})
    return redirect('accounts/login')


@login_required
def profile(request):
    return render(request, 'pages/profile.html',{});
