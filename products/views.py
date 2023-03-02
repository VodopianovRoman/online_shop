from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
PRODUCT_HTML = 'products/product.html'
PRODUCTS_PAGE = 'products/products_page.html'


def products(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(f'Session key: {request.session.session_key}')

    form = ReviewsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.id_of_product = product_id
        review.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    reviews_for_user = Reviews.objects.filter(id_of_product=product_id)

    return render(request, PRODUCT_HTML, locals())


def products_page(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)

    if 'sety' in request.GET:
        products_images_sets = products_images.filter(product__category__id=2)

    if 'pizza' in request.GET:
        products_images_pizza = products_images.filter(product__category__id=1)

    return render(request, PRODUCTS_PAGE, locals())