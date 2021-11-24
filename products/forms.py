from django import forms
from django.forms import fields
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price'
        ]


class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={
                    "placeholder": "Your title"
    })) # default required = True
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
                    "placeholder": "Your description",
                    "class": "new-class name",
                    "id": "input-id",
                    "rows": 20,
                    "cols":
                    120
    }))
    price       = forms.DecimalField(initial=199.99)