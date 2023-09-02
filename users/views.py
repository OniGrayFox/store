from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.models import User
from users.forms import UserLoginForm
from django.urls import reverse


def login_view(request):

    if request.POST:
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    args = {
        'form': form,

            }
    return render(request, "users/login.html", args)


def registration_view(request):
    return render(request, "users/register.html")
