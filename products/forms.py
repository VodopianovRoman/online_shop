from django import forms
from .models import *


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["review", "user_name"]
