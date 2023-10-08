from django.shortcuts import render
from .models import Product, ProductCategory, Basket
from users.models import User
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic.list import ListView




class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context



# def index_view(request):
#     args = {
#         'title': 'Test title',
#         'username': 'artem',
#     }
#     return render(request, "products/index.html", args)

class ProductsListView(ListView):
    model = Product
    template_name = "products/products.html"
    paginate_by = 2

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'Store - каталог'
        context['categories'] = ProductCategory.objects.all()
        return context



# def products_view(request, category_id=None, page_number=1):
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)  # К id можно через _ слэш а не через __
#     else:
#         products = Product.objects.all()
#     per_page = 2
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)
#
#
#     args = {
#         'products': products_paginator,
#         'categories': ProductCategory.objects.all()
#
#     }
#     return render(request, "products/products.html", args)



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
