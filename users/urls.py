from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path("users/", sign_up, name='users-sign-up'),
    path("profile/", profile, name='users-profile'),
    path("", auth_view.LoginView.as_view(template_name = 'users/login.html'), name='users-login'),
    path("logout/",logout_view, name='users-logout'),
    path("logoUt/", LogoUt, name='LogoUT')
]
