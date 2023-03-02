from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.orders, name='orders'),
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
    re_path(r'^checkout_delivery$', views.checkout_delivery, name='checkout_delivery'),
]
