from django.contrib import admin

from django.urls import path
from users.views import login_view, registration_view, profile_view, logout_view

app_name = 'users'

urlpatterns = [

    path('login', login_view, name='login'),
    path('register', registration_view, name='register'),
    path('profile', profile_view, name='profile'),
    path('logout', logout_view, name='logout'),
]
