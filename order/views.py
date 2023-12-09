from django.shortcuts import render
#from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.
from .forms import OrderForm

class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm