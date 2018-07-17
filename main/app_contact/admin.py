# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app_contact.models import App_contact

class PageAdmin(admin.ModelAdmin):
    list_display = ('Full_Nane', 'Phone_number1','Phone_number2','Email') # какие поля выводить в админке


# Register your models here.
# добавить модель Page в админку

admin.site.register(App_contact)
