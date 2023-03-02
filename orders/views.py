from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from products.models import ProductImage
from .models import *
from .forms import CheckoutContactForm


CHECKOUT_HTML = 'orders/checkout.html'
CHECKOUT_DELIVERY_HTML = 'orders/checkout_delivery.html'
THNK_PAGE_HTML = 'orders/thnk_page.html'


def orders(request):
    pass


def basket_adding(request):
    return_dict = {}

    session_key = request.session.session_key

    print(f'REQUEST POST: {request.POST}')
    data = request.POST
    product_id = data.get('product_id')
    product_quantity = data.get('product_quantity')
    is_delete = data.get('is_delete')

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True,
                                                                     order=None,
                                                                     defaults={'count': product_quantity})
        if not created:
            new_product.count += int(product_quantity)
            new_product.save(force_update=True)

    # common code for 2 cases
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_number = products_in_basket.count()
    return_dict['products_total_number'] = products_total_number
    return_dict['products'] = list()

    for product in products_in_basket:
        product_dict = {}
        product_dict['product_id'] = product.id
        product_dict['product_name'] = product.product.name
        product_dict['product_quantity'] = product.count
        product_dict['product_total_price'] = product.total_price
        return_dict['products'].append(product_dict)  # throwing to ajax in scripts.js in success part

    return JsonResponse(return_dict)  # throwing to ajax in scripts.js


def checkout(request):
    session_key = request.session.session_key

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True).exclude(order__isnull=False) # order__isnull=False -> exclude products already on order

    form = CheckoutContactForm(request.POST or None)

    total_price_of_basket = 0
    for product_in_basket in products_in_basket:
        total_price_of_basket += product_in_basket.total_price

    if request.POST:
        print(f'Request from Checkout:  {request.POST}')
        if form.is_valid():
            data = request.POST
            name = data.get('name')
            phone = data.get('phone')

            user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

            for k, v in data.items():
                if k.startswith('product_in_basket_'):
                    product_in_basket_id = k.split('product_in_basket_')[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)

                    product_in_basket.count = v  # increase quantity of products in ProductInOrder and in Order
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, count=product_in_basket.count,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)

                    created = True
                    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    
        else:
            pass
    return render(request, CHECKOUT_HTML, locals())


def checkout_delivery(request):
    session_key = request.session.session_key

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)

    total_price_of_basket = 0
    for product_in_basket in products_in_basket:
        total_price_of_basket += product_in_basket.total_price

    return render(request, CHECKOUT_DELIVERY_HTML, locals())

