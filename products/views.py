# views.py
from django.shortcuts import render
from .models import Product


def product_index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/index.html", context)
