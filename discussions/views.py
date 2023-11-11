from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from django.shortcuts import render, redirect

def teste(request):
    return HttpResponse("ok")

def posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
    else:
        posts = []
    return HttpResponse(posts)

def homepage(request):
    return render(request, 'pages/homepage.html')