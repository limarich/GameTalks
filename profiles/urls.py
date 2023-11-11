from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('login', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('accounts/profile/', views.profile, name='account_profile'),
]
