from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^product/(?P<product_id>\w+)/$', views.products, name='product'),
    re_path(r'^our-products/$', views.products_page, name='our-products'),
]