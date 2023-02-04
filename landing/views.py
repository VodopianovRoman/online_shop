from django.shortcuts import render

from .forms import *

# Create your views here.
LANDING_HTML = "landing/landing.html"


def landing(request):
    context = {}
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        subscriber_obj = form.save()
        context["subscribed"] = True

    context["form"] = form
    return render(request, LANDING_HTML, context=context)
