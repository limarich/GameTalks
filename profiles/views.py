from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from allauth.account.forms import LoginForm, SignupForm
from discussions.models import Post, Comment,Tag
from .models import Profile

def login(request):
    login_form = LoginForm()
    signup_form = SignupForm()
    return render(request, 'pages/login.html', {'login_form': login_form, 'signup_form': signup_form})

@login_required
def profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    user_posts = Post.objects.filter(user=request.user)
    user_comments = Comment.objects.filter(user=request.user)
    
    print(user_profile.avatar_img)
    
    posts_with_tags = []
    for post in user_posts:
        tags_from_post = post.tag_set.all()
        post_tags = {'post_content': post, 'tags': tags_from_post}
        posts_with_tags.append(post_tags)
        
    
    return render(request, 'pages/profile.html',{'user_profile': user_profile, 'user_posts': posts_with_tags,'user_posts_count': user_posts.count(), 'user_comments_count': user_comments.count()});
 