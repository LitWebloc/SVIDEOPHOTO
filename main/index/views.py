# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def portfolio(request):
    return render(request, "portfolio.html")

def price(request):
    return render(request, "price.html")

def comments(request):
    return render(request, "comments.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")
