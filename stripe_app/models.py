# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Order(models.Model):
    name        = models.CharField(max_length=234)
    year        = models.CharField(max_length=111)
    charge_id   = models.CharField(max_length=234)