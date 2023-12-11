import stripe

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.conf import settings

from .forms import OrderForm

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('order:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price': '{{ PRICE_ID }}',
                'quanity':1,
            },
            ],
            mode='payment',
            success_url=settings.DOMAIN_NAME + '/success.html',
            cancel_url=settings.DOMAIN_NAME + '/cancel.html',


        )

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
#class OrderSuccess(TemplateView):
