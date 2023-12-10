from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from allauth.account.forms import LoginForm, SignupForm
from discussions.models import Post, Comment,Tag
from .models import Profile
from datetime import datetime

def login(request):
    login_form = LoginForm()
    signup_form = SignupForm()
    return render(request, 'pages/login.html', {'login_form': login_form, 'signup_form': signup_form})

@login_required
def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'GET':
        user_has_profile = bool(user_profile)
        
        user_posts = Post.objects.filter(user=request.user).prefetch_related('tags')
        user_comments = Comment.objects.filter(user=request.user)
        
        if(user_profile and user_profile.birth_day): 
            user_profile.birth_day = user_profile.birth_day.strftime("%d/%m/%Y")
            user_profile.created_at = user_profile.created_at.strftime("%d/%m/%Y")
        
        for post in user_posts:
            print(f"Post: {post.title}")
            for tag in post.tags.all():
                print(f"Tag: {tag.title}")
        
        return render(request, 'pages/profile.html', {
            'user_profile': user_profile,
            'user_posts': user_posts,
            'user_posts_count': user_posts.count(),
            'user_comments_count': user_comments.count(),
            'user_has_profile': user_has_profile
        })
    if request.method == 'POST':
        if user_profile:
            birth_day = request.POST.get('birth_day')

            if birth_day:
                birth_day_formatted = datetime.strptime(birth_day, '%Y-%m-%d').date()
                user_profile.birth_day = birth_day_formatted.strftime('%Y-%m-%d')

            user_profile.user_name = request.POST.get('user_name')
            user_profile.email = request.POST.get('email')
            user_profile.bio = request.POST.get('bio')
            user_profile.avatar_img = request.FILES.get('avatar_img')
            user_profile.save()
        else:
            new_profile = Profile(
                user=request.user,
                user_name=request.POST.get('user_name'),
                email=request.POST.get('email'),
                bio=request.POST.get('bio'),
                avatar_img=request.FILES.get('avatar_img')
            )
            birth_day = request.POST.get('birth_day')

            if birth_day:
                birth_day_formatted = datetime.strptime(birth_day, '%Y-%m-%d').date()
                new_profile.birth_day = birth_day_formatted.strftime('%Y-%m-%d')

            new_profile.save()

        return redirect('/profile')
 