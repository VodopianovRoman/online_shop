from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
PRODUCT_HTML = 'products/product.html'


def products(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ReviewsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.id_of_product = product_id
        review.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    reviews_for_user = Reviews.objects.filter(id_of_product=product_id)

    return render(request, PRODUCT_HTML, locals())
