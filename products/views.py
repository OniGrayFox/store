from django.shortcuts import render
from .models import Product, ProductCategory, Basket
from users.models import User
from django.http.response import HttpResponseRedirect


def index_view(request):

    args = {
        'title': 'Test title',
            'username': 'artem',
            }
    return render(request, "products/index.html", args)


def products_view(request):
    args = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()

    }
    return render(request, "products/products.html", args)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product,quantity=1)
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])