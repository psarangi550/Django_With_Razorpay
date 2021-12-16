from django import forms
from .models import Coffee

class CoffeeForm(forms.ModelForm):
    class Meta:
        model=Coffee
        fields="__all__"
        exclude = ("order_id","paid")
