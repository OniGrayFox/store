from django.shortcuts import render
from .models import Product, ProductCategory, Basket
from users.models import User
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



def index_view(request):
    args = {
        'title': 'Test title',
        'username': 'artem',
    }
    return render(request, "products/index.html", args)


def products_view(request, category_id=None, page_number=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)  # К id можно через _ слэш а не через __
    else:
        products = Product.objects.all()
    per_page = 2
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)


    args = {
        'products': products_paginator,
        'categories': ProductCategory.objects.all()

    }
    return render(request, "products/products.html", args)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
