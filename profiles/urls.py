from django.urls import path
from . import views
from allauth.account.views import LogoutView

app_name = "profiles"

urlpatterns = [
    path('login', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='account_profile'),
]
