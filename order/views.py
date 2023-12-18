import stripe

from http import HTTPStatus
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .forms import OrderForm

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'orders/success.html'


class CancelView(TemplateView):
    template_name = 'orders/cancled.html'


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('order:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price': 'price_1OLnKHCiHd4VNJb0ZK8k3ibE',
                'quantity': 1,
            },
            ],
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url="{}{}".format(settings.DOMAIN_NAME, reverse_lazy('order:order_success')),
            cancel_url="{}{}".format(settings.DOMAIN_NAME, reverse_lazy('order:order_cancel')),

        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Passed signature verification
    return HttpResponse(status=200)


def fulfill_order(line_items):
  order_id = line_items.metadata.order_id

  print(order_id)