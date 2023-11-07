from django.db import models
from django.contrib.auth.models import User

def upload_avatar_img(instance, filename):
    return f"{instance.user.id}-{filename}"

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20, null=True)
    birth_day = models.DateField(null=True)
    email = models.EmailField(null=True)
    bio = models.CharField(max_length=200, null=True)
    is_moderator = models.BooleanField(default=False)
    last_access = models.DateField(auto_now=True)
    avatar_img = models.ImageField(upload_to=upload_avatar_img ,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

