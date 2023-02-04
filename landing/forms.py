from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ["email", "name"]
        # labels = {
        #          "email": "Яка твоя електрона пошта?",
        #          "name": "Як тебе звати?"
        #          }