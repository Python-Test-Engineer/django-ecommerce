# views.py
from django.shortcuts import render
from .models import Order


def order_index(request):

    context = {}
    return render(request, "orders/index.html", context)
