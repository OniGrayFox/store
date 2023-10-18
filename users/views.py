from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse, reverse_lazy
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm



class UserRegistrationView(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

