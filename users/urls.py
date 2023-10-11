from django.contrib import admin

from django.urls import path
from users.views import login_view, UserRegistrationView, UserProfileView, logout_view

from django.contrib.auth.decorators import login_required
app_name = 'users'

urlpatterns = [

    path('login/', login_view, name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout_view, name='logout'),
]
