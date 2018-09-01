# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.conf import settings
from .models import Order
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def payment_form(request):

    context = { "stripe_key": settings.STRIPE_PUBLIC_KEY }
    return render(request, "stripetemplate.html", context)

def thankyou(request):
    context = {}
    return render(request, "thankyou.html", context)


def checkout(request):

    new_order = Order(
        name = "Veg Pizza",
        year  = '2018'
    )

    if request.method == "POST":
        token = request.POST.get("stripeToken")

    try:
        charge  = stripe.Charge.create(
            amount      = 100,
            currency    = "usd",
            source      = token,
            description = "the website charged the user"
        )

        new_order.charge_id   = charge.id

    except stripe.error.CardError as ce:
        return False, ce

    else:
        new_order.save()
        return redirect('thankyou_page')
        # The payment was successful, user's card was charged. 
        # user can now redirected to any page you wish.
