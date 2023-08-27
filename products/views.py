from django.shortcuts import render
from .models import Product
# Create your views here.
def index_view(request):

    args = {
        'title': 'Test title',
            'username': 'artem',
            }
    return render(request, "products/index.html", args)

def products_view(request):
    args = {
        'products': Product.objects.all()

    }
    return render(request, "products/products.html", args)