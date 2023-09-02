from django.contrib import admin

from django.urls import path
from users.views import login_view, registration_view

app_name = 'users'

urlpatterns = [

    path('/login', login_view, name='login'),
    path('/register', registration_view, name='register'),

]
