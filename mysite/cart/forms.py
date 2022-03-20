

from django import forms
from django.forms.widgets import NumberInput


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
    class Meta:
        fields = ['quantity','update']
        widgets = {
            'quantity': NumberInput(attrs={
                'class': 'cart-plus-minus',
                'value': '2',
                'title': 'Number for card'
            })
        }

