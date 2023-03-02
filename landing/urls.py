from django.urls import path, include
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^contact/$', views.contact, name='contact'),
    # path('', views.home, name='home'),
    path('landing', views.landing, name='landing'),
]