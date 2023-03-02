from django import forms
from .models import *


# class OrderForm(forms.ModelForm):
#
#     class Meta:
#         model = Order


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)