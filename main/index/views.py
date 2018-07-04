# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def portfolio(request):
    return render(request, "portfolio.html")

def coins(request):
    return render(request, "coins.html")

def reviews(request):
    return render(request, "reviews.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")
