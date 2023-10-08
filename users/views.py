from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse, reverse_lazy
from products.models import Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView



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



class UserRegistrationView(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')



# def registration_view(request):
#     if request.POST:
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Поздравляем! пользователь создан!")
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#
#     args = {
#
#         "form": form,
#
#     }
#     return render(request, "users/register.html", args)

@login_required
def profile_view(request):
    if request.POST:
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)

    args = {
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),

            }
    return render(request, "users/profile.html", args)


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


