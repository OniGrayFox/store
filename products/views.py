from django.shortcuts import render

# Create your views here.
def index_view(request):
    args = {}
    return render(request, "products/index.html", args)

def products_view(request):
    args = {}
    return render(request, "products/products.html", args)