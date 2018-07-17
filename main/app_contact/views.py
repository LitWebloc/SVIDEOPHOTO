# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import App_contact
# Create your views here.

def contacts(request):
    contacts = App_contact.objects.all()
    return render(request, "index.html", {'contacts':contacts })
