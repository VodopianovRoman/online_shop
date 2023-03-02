from django.shortcuts import render

from .forms import *
from products.models import *

# Create your views here.
LANDING_HTML = "landing/landing.html"
HOME_HTML = "landing/home.html"
CONTACT_HTML = "landing/contact.html"


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_popular = products_images.filter(product__popular=True, product__is_active=True)
    products_images_pizza = products_images.filter(product__category__id=1)
    products_images_sets = products_images.filter(product__category__id=2)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, HOME_HTML, locals())


def contact(request):

    return render(request, CONTACT_HTML, locals())


def landing(request):
    context = {}
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        subscriber_obj = form.save()
        context["subscribed"] = True

    context["form"] = form
    return render(request, LANDING_HTML, context=context)
