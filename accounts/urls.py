from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import path

from .views import signup

urlpatterns = [
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
