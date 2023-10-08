from django.contrib import admin

from django.urls import path
from users.views import login_view, UserRegistrationView, profile_view, logout_view

app_name = 'users'

urlpatterns = [

    path('login', login_view, name='login'),
    path('register', UserRegistrationView.as_view(), name='register'),
    path('profile', profile_view, name='profile'),
    path('logout', logout_view, name='logout'),
]
