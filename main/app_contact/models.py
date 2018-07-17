# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class App_contact(models.Model):
    Full_Nane       = models.CharField(max_length=200)
    Phone_number1   = models.CharField(max_length=200)
    Phone_number2   = models.CharField(max_length=200)
    Email           = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.Full_Nane
